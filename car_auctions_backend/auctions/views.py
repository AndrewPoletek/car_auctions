from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import AuctionForm
from .models import Auction, PriceProposal
from django.views.generic.edit import FormView
from django.views.generic import DetailView

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
        return context
