# pricing_app/admin.py
from django.contrib import admin
from django.contrib.admin.models import LogEntry, ADDITION, CHANGE
from .models import PricingConfiguration, ConfigurationChangeLog
from .forms import PricingConfigurationForm

class PricingConfigurationAdmin(admin.ModelAdmin):
    form = PricingConfigurationForm

    def save_model(self, request, obj, form, change):
        # Save the user making the change in the form's save method
        obj = form.save(commit=True, user=request.user)
        super().save_model(request, obj, form, change)

admin.site.register(PricingConfiguration, PricingConfigurationAdmin)
admin.site.register(ConfigurationChangeLog)
