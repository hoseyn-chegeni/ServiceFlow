from django.db import models


# Create your models here.
class Asset(models.Model):
    name = models.CharField(max_length=255)
    type = models.ForeignKey(
        "AssetType", on_delete=models.SET_NULL, blank=True, null=True
    )
    manufacturer = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=50, unique=True)
    # purchase_date = models.DateField()
    # warranty_expiry_date = models.DateField(blank=True, null=True)
    location = models.CharField(max_length=100)
    assigned_user = models.ForeignKey(
        "accounts.User", on_delete=models.SET_NULL, blank=True, null=True
    )
    status = models.ForeignKey(
        "AssetStatus", on_delete=models.SET_NULL, blank=True, null=True
    )
    condition = models.ForeignKey(
        "AssetCondition", on_delete=models.SET_NULL, blank=True, null=True
    )
    maintenance_schedule = models.CharField(max_length=100, blank=True, null=True)
    # last_maintenance_date = models.DateField()
    purchase_cost = models.DecimalField(max_digits=10, decimal_places=2)
    current_value = models.DecimalField(max_digits=10, decimal_places=2)
    depreciation_rate = models.DecimalField(max_digits=5, decimal_places=2)
    assigned_ip_address = models.GenericIPAddressField(null=True, blank=True)
    software_installed = models.TextField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    created_by = models.ForeignKey(
        "accounts.User",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="asset_creator",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
