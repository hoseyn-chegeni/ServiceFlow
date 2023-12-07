from django.db import models


# Create your models here.
def generate_pk():
    pass


class Organization(models.Model):
    name = models.CharField(
        max_length=255,
    )
    address = models.TextField(blank=True, null=True)
    # city = 0
    # state = 0
    # country = 0
    postal_code = models.CharField(
        max_length=20,
    )
    phone_number = models.CharField(
        max_length=20,
    )
    email = models.EmailField()
    website = models.URLField()
    industry = models.CharField(
        max_length=255,
    )
    employee_count = models.PositiveIntegerField()
    # department = 0
    founding_date = models.DateField()
    parent_organization = models.ForeignKey(
        "self", on_delete=models.SET_NULL, blank=True, null=True, related_name="parent"
    )
    subsidiaries = models.ManyToManyField("self", blank=True)
    legal_entity_type = models.CharField(
        max_length=255,
    )
    tax_id_number = models.CharField(
        max_length=255,
    )
    registration_number = models.CharField(max_length=50)
    registration_date = models.DateField()
    logo = models.ImageField(upload_to="images", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        "accounts.User", models.SET_NULL, blank=True, null=True
    )

    def __str__(self):
        return self.name


def generate_dept_pk():
    pass
