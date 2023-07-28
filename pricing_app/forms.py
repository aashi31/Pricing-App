# pricing_app/forms.py
from django import forms
from .models import PricingConfiguration, ConfigurationChangeLog
from django.contrib.admin.models import LogEntry, ADDITION, CHANGE

class PricingConfigurationForm(forms.ModelForm):
    class Meta:
        model = PricingConfiguration
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        is_enabled = cleaned_data.get('is_enabled')
        days_of_week = cleaned_data.get('days_of_week')
        
        # Validate that there is at least one day of the week selected when enabled
        if is_enabled and not days_of_week:
            raise forms.ValidationError('You must select at least one day of the week when the configuration is enabled.')
        
        return cleaned_data

    def save(self, commit=True, user=None):
        instance = super().save(commit=commit)
        
        if commit and user:
            action = ADDITION if instance._state.adding else CHANGE
            ConfigurationChangeLog.objects.create(user=user, configuration=instance, action=action)

        return instance

