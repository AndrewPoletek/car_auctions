from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Auction(models.Model):
    BODY_TYPES = [
        ('SEDAN', 'SEDAN'),
        ('HATCHBACK', 'HATCHBACK'),
        ('KOMBI', 'KOMBI')
    ]
    PETROL_TYPES = [
        ('ELECTRIC', 'ELEKTRTYCZY'),
        ('PETROL', 'BENZYNA'),
        ('HYBRID', 'HYBRYDOWY'),
        ('DIESEL', 'DIESEL'),
        ('LPG', 'LPG'),
        ('CNG', 'CNG'),
    ]

    title = models.CharField(max_length=250)
    description = models.TextField(max_length=10000)
    engine_power = models.IntegerField()
    engine_capacity = models.IntegerField()
    type_body= models.CharField(choices=BODY_TYPES, max_length=150)
    production_year = models.IntegerField()
    mileage = models.IntegerField()
    petrol_type = models.CharField(choices=PETROL_TYPES, max_length=150)
    start_price = models.DecimalField(decimal_places=2, max_digits=99)
    start_date = models.DateField()
    end_date = models.DateField()
    active = models.BooleanField(default=True)


class PriceProposal(models.Model):
    price = models.DecimalField(decimal_places=2, max_digits=99)
    owner = models.ForeignKey(User, on_delete=models.PROTECT)
    auction = models.ForeignKey(Auction, on_delete=models.PROTECT)
    datetime_propose = models.DateTimeField(auto_now_add=True)