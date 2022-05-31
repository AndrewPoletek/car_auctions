from django.db import models

# Create your models here.

class Auction(models.Model):
    ENGINE_POWER_UNIT = [
        ('KM', 'Konie Mechaniczne'),
        ('KW', 'Kilowaty'),
    ]
    BODY_TYPES = [
        ('SEDAN', 'SEDAN'),
        ('HATCHBACK', 'HATCHBACK'),
        ('KOMBI', 'KOMBI')
    ]
    MILEAGE_TYPES = [
        ('km', 'KILOMETRY'),
        ('mile', 'MILE')
    ]
    PETROL_TYPES = [
        ('ELECTRIC', 'ELEKTRTYCZY'),
        ('PETROL', 'BENZYNA'),
        ('HYBRID', 'HYBRYDOWY'),
        ('DIESEL', 'DIESEL'),
        ('LPG', 'LPG'),
        ('CNG', 'CNG'),
    ]

    name = models.CharField(max_length=250)
    description = models.TextField(max_length=10000)
    color = models.CharField(max_length=50)
    engine_power = models.IntegerField()
    engine_power_unit = models.CharField(choices=ENGINE_POWER_UNIT, max_length=150)
    engine_capacity = models.IntegerField()
    type_body= models.CharField(choices=BODY_TYPES, max_length=150)
    production_year = models.IntegerField()
    mileage = models.IntegerField()
    mileage_type = models.CharField(choices=MILEAGE_TYPES, max_length=150)
    petrol_type = models.CharField(choices=PETROL_TYPES, max_length=150)


