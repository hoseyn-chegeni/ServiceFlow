from django.db import models


class Component(models.Model):
    company = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images", blank=True, null=True)
    serial = models.CharField(max_length=100)
    category = models.ForeignKey(
        "ComponentCategory", on_delete=models.SET_NULL, blank=True, null=True
    )
    supplier = models.CharField(max_length=100)
    total = models.PositiveIntegerField(default=0)
    remaining = models.PositiveIntegerField(default=0)
    min_quantity = models.PositiveIntegerField(default=0)
    location = models.CharField(max_length=100)
    order_number = models.CharField(max_length=100)
    purchase_date = models.DateField()
    purchase_cost = models.DecimalField(max_digits=10, decimal_places=2)
    notes = models.TextField(blank=True)
    created_by = models.ForeignKey(
        "accounts.User", on_delete=models.SET_NULL, blank=True, null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class ComponentCategory(models.Model):
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
