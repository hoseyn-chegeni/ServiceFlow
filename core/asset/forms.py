from django import forms
from .models.asset import Asset
from .models.asset_status import AssetStatus
from .models.asset_type import AssetType
from .models.accessory import Accessory, AccessoryCategory


class CreateAssetForm(forms.ModelForm):
    class Meta:
        model = Asset
        fields = (
            "name",
            "type",
            "manufacturer",
            "model",
            "serial_number",
            "location",
            "assigned_user",
            "status",
            "maintenance_schedule",
            "purchase_cost",
            "current_value",
            "depreciation_rate",
            "assigned_ip_address",
            "software_installed",
            "notes",
            "imei",
            "image",
            "supplier",
            "warranty",
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


class CreateAccessoryForm(forms.ModelForm):
    class Meta:
        model = Accessory
        fields = (
            "image",
            "company",
            "name",
            "category",
            "model_number",
            "manufacturer",
            "supplier",
            "location",
            "total",
            "available",
            "checked_out",
            "min_quantity",
            "purchase_date",
            "purchase_cost",
            "order_number",
            "notes",
            "in_out",
        )