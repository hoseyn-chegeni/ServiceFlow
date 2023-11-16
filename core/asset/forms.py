from django import forms
from .models.asset import Asset
from .models.asset_status import AssetStatus
from .models.asset_condition import AssetCondition
from .models.asset_type import AssetType


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

class CreateAssetStatusForm(forms.ModelForm):
    class Meta:
        model = AssetStatus
        fields = (
            "name",
            "description",
        )

class CreateAssetTypeForm(forms.ModelForm):
    class Meta:
        model = AssetType
        fields = (
            "name",
            "description",
        )

class CreateAssetConditionForm(forms.ModelForm):
    class Meta:
        model = AssetCondition
        fields = (
            "name",
            "description",
        )
 