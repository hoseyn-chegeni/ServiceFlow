from django.db import models


class Accessory(models.Model):
    image = models.ImageField(upload_to="images", blank=True, null=True)
    company = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    category = models.ForeignKey(
        "AccessoryCategory", on_delete=models.SET_NULL, blank=True, null=True
    )
    model_number = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    supplier = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    total = models.PositiveIntegerField(default=0)
    available = models.PositiveIntegerField(default=0)
    checked_out = models.PositiveIntegerField(default=0)
    min_quantity = models.PositiveIntegerField(default=0)
    purchase_date = models.DateField()
    purchase_cost = models.DecimalField(max_digits=10, decimal_places=2)
    order_number = models.CharField(max_length=100)
    notes = models.TextField(blank=True)
    in_out = models.CharField(max_length=10)
    created_by = models.ForeignKey(
        "accounts.User", on_delete=models.SET_NULL, blank=True, null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class AccessoryCategory(models.Model):
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
