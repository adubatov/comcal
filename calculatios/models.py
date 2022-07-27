from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
class Deal(models.Model): #Song
    bx_deal_id = models.PositiveIntegerField(unique=True)
    bx_user_id = models.PositiveIntegerField()
    company_name = models.TextField()
    deal_name = models.TextField()

    cost = models.PositiveIntegerField()
    cost_currency_is_usd = models.BooleanField()
    logistics = models.FloatField()
    logistics_currency_is_usd = models.BooleanField()
    logistics_is_standard = models.BooleanField()
    engineer_cost = models.PositiveIntegerField()
    engineer_involved = models.BooleanField()

    income = models.PositiveIntegerField()
    income_currency_is_usd = models.BooleanField()


class Calculation(models.Model): #Playlist
    title = models.TextField(null=True)
    user_id = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    usd_rate = models.FloatField()
    usd_rate_internal = models.FloatField()


class CalculationDeals(models.Model): #Playlist songs
    calculation_id = models.ForeignKey(Calculation, on_delete=models.CASCADE)
    deal_id = models.ForeignKey(Deal, on_delete=models.CASCADE)
