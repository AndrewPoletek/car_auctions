from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import AuctionForm
from .models import Auction, PriceProposal
from django.views.generic.edit import FormView
from django.views.generic import DetailView
from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

# Create your views here.

class AuctionsList(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        auctions = Auction.objects.filter(active=True)
        return render(request, 'auctions_list.html', {'auctions':auctions})

class CreateAuction(LoginRequiredMixin, FormView):
    template_name = 'create_auction.html'
    form_class = AuctionForm
    success_url = '/'
    def form_valid(self, form):
        new_auction = form.save(commit=False)
        new_auction.owner = self.request.user
        new_auction.active=True
        new_auction.save()
        return super().form_valid(form)

class AuctionView(LoginRequiredMixin, DetailView):
    model = Auction
    context_object_name = 'auction'
    template_name = 'auction_view.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        still_active = True
        if self.object.end_date < timezone.now():
            still_active = False
        context['still_active'] = still_active
        context['proposals'] = PriceProposal.objects.filter(auction=self.object).order_by('-datetime_propose')
        return context

class ProposalPriceView(APIView):
    authentication_classes = [authentication.SessionAuthentication,]
    permission_classes = [permissions.IsAuthenticated,]
    def post(self, request):
        auction = Auction.objects.get(pk=request.data['auction_id'])
        if auction.end_date < timezone.now():
            return Response({'error': 'Licytacja Zakończona'}, status=402)
        proposal_price = request.data['price']
        check_price = PriceProposal.objects.filter(price__gte=proposal_price, auction=auction).count()
        if check_price > 0:
            return Response({'error':'Zbyt mała kwota'}, status=403)
        else:
            PriceProposal.objects.create(price=proposal_price, auction=auction, owner=request.user)
            return Response({"status": "OK"}, status=201)

