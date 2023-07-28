# pricing_app/models.py
from django.db import models
from django.contrib.auth.models import User

class PricingConfiguration(models.Model):
    name = models.CharField(max_length=100, unique=True)
    distance_base_price = models.DecimalField(max_digits=8, decimal_places=2)
    distance_additional_price = models.DecimalField(max_digits=8, decimal_places=2)
    time_multiplier_factor = models.DecimalField(max_digits=8, decimal_places=2)
    waiting_charges = models.DecimalField(max_digits=8, decimal_places=2)
    days_of_week = models.CharField(max_length=50, help_text="Comma-separated days (e.g., Mon,Tue)")
    is_enabled = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class ConfigurationChangeLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    configuration = models.ForeignKey("PricingConfiguration", on_delete=models.CASCADE)  # Use "self" as string
    timestamp = models.DateTimeField(auto_now_add=True)
    action = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.configuration.name} - {self.action} by {self.user.username}"

