from django.contrib import admin
from .models import Auction, PriceProposal

# Register your models here.

@admin.register(Auction)
class AuctionAdmin(admin.ModelAdmin):
    pass