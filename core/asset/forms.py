from django import forms
from .models.asset import Asset


class CreateAssetForm(forms.ModelForm):
    class Meta:
        model = Asset
        fields = (
            "name",
            "type",
            "manufacturer",
            "model",
            "location",
            "assigned_user",
            "status",
            "condition",
            "maintenance_schedule",
            "purchase_cost",
            "current_value",
            "depreciation_rate",
            "assigned_ip_address",
            "software_installed",
            "notes",
        )
