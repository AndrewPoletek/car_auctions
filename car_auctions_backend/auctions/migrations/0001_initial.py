# Generated by Django 3.2.13 on 2022-06-16 05:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Auction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('description', models.TextField(max_length=10000)),
                ('engine_power', models.IntegerField()),
                ('engine_capacity', models.IntegerField()),
                ('type_body', models.CharField(choices=[('SEDAN', 'SEDAN'), ('HATCHBACK', 'HATCHBACK'), ('KOMBI', 'KOMBI')], max_length=150)),
                ('production_year', models.IntegerField()),
                ('mileage', models.IntegerField()),
                ('petrol_type', models.CharField(choices=[('ELECTRIC', 'ELEKTRTYCZY'), ('PETROL', 'BENZYNA'), ('HYBRID', 'HYBRYDOWY'), ('DIESEL', 'DIESEL'), ('LPG', 'LPG'), ('CNG', 'CNG')], max_length=150)),
                ('start_price', models.DecimalField(decimal_places=2, max_digits=99)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='PriceProposal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=99)),
                ('datetime_propose', models.DateTimeField(auto_now_add=True)),
                ('auction', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='auctions.auction')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
