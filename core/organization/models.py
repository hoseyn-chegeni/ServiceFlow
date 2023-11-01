from django.db import models


# Create your models here.
def generate_pk():
    if Organization.objects.last() is not None:
        number = (Organization.objects.last().id) + 1
        return f"ORG-{number}"
    else:
        return f"ORG-1"


class Organization(models.Model):
    org = models.CharField(
        default=generate_pk, max_length=255, unique=True, editable=False
    )
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
    logo = models.ImageField(upload_to="image", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        "accounts.User", models.SET_NULL, blank=True, null=True
    )

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank= True, null=True)
    manager = models.ForeignKey('accounts.User', on_delete=models.SET_NULL, blank=True, null=True)
    active_status = models.BooleanField(default=True)
    organization = models.ForeignKey('organization.Organization', on_delete=models.SET_NULL, blank=True,null=True)