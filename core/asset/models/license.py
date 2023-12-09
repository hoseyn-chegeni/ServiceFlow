from django.db import models


class License(models.Model):
    license_key = models.CharField(max_length=100)
    software_name = models.CharField(max_length=100)
    category = models.ForeignKey(
        "LicenseCategory", on_delete=models.SET_NULL, blank=True, null=True
    )
    product_key = models.CharField(max_length=100)
    seats = models.IntegerField()
    company = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    licensed_to_name = models.CharField(max_length=100)
    licensed_to_email = models.EmailField()
    reassignable = models.BooleanField(default=False)
    supplier = models.CharField(max_length=100)
    order_number = models.CharField(max_length=100)
    purchase_cost = models.DecimalField(max_digits=10, decimal_places=2)
    purchase_date = models.DateField()
    expiration_date = models.DateField()
    termination_date = models.DateField(null=True, blank=True)
    purchase_order_number = models.CharField(max_length=100, null=True, blank=True)
    depreciation = models.DecimalField(max_digits=10, decimal_places=2)
    maintained = models.BooleanField(default=True)
    notes = models.TextField(blank=True)
    created_by = models.ForeignKey(
        "accounts.User", on_delete=models.SET_NULL, blank=True, null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.software_name


class LicenseCategory(models.Model):
    name = models.CharField(
        max_length=255,
    )
    description = models.TextField(
        blank=True,
        null=True,
    )
    created_by = models.ForeignKey(
        "accounts.User", on_delete=models.SET_NULL, blank=True, null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name
