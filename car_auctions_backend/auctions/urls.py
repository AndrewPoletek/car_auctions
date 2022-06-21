from django.urls import path
from .views import AuctionsList, CreateAuction, AuctionView, ProposalPriceView

urlpatterns = [
    path('', AuctionsList.as_view()),
    path('create_auction', CreateAuction.as_view()),
    path('auction_view/<int:pk>', AuctionView.as_view()),
    path('bid', ProposalPriceView.as_view())
]