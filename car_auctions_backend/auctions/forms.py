from django.forms import ModelForm
from django import forms
from .models import Auction


class AuctionForm(ModelForm):
    start_date = forms.DateField(widget=forms.SelectDateWidget())
    end_date = forms.DateField(widget=forms.SelectDateWidget())
    class Meta:
        model = Auction
        exclude = ['owner', 'active']
        # fields = ['title', 'description', 'engine_power', 'engine_capacity', 'type_body', 'production_year', 'mileage',
        #           'petrol_type', 'start_price', 'start_date', 'end_date']
        # fields = '__all__'