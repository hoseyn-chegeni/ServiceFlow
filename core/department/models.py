from django.db import models


# Create your models here.
def generate_pk():
    if Department.objects.last() is not None:
        number = (Department.objects.last().id) + 1
        return f"DEPT-{number}"
    else:
        return f"DEPT-1"


class Department(models.Model):
    dept = models.CharField(
        default=generate_pk, max_length=255, unique=True, editable=False
    )
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    manager = models.ForeignKey(
        "accounts.User", on_delete=models.SET_NULL, blank=True, null=True
    )
    active_status = models.BooleanField(default=True)
    organization = models.ForeignKey(
        "organization.Organization",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="department",
    )
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    created_by = models.ForeignKey(
        "accounts.User",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="creator",
    )

    def __str__(self):
        return self.name
