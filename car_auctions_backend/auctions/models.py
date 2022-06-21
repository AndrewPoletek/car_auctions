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

    title = models.CharField(max_length=250, verbose_name="Tytuł aukcji")
    description = models.TextField(max_length=10000, verbose_name="Opis pojazdu")
    engine_power = models.IntegerField(verbose_name="Moc silnika")
    engine_capacity = models.IntegerField(verbose_name="Pojemność silnika")
    type_body= models.CharField(choices=BODY_TYPES, max_length=150, verbose_name="Rodzaj nadwozia")
    production_year = models.IntegerField(verbose_name="Data produkcji")
    mileage = models.IntegerField(verbose_name="Przebieg")
    petrol_type = models.CharField(choices=PETROL_TYPES, max_length=150, verbose_name="Rodzaj paliwa")
    start_price = models.DecimalField(decimal_places=2, max_digits=99, verbose_name="Cena wywoławcza")
    start_date = models.DateField(verbose_name="Początek aukcji")
    end_date = models.DateField(verbose_name="Koniec aukcji")
    active = models.BooleanField(default=True, verbose_name="Czy aktywować?")
    owner = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name="Właściciel")
    photo = models.ImageField(null=True, upload_to='media/')

    @property
    def get_last_price(self):
        price = self.priceproposal_set.last()
        if price:
            return price.price
        else:
            return self.start_price


class PriceProposal(models.Model):
    price = models.DecimalField(decimal_places=2, max_digits=99)
    owner = models.ForeignKey(User, on_delete=models.PROTECT)
    auction = models.ForeignKey(Auction, on_delete=models.PROTECT)
    datetime_propose = models.DateTimeField(auto_now_add=True)