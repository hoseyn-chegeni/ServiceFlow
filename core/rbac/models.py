from django.db import models
from django.contrib.auth.models import Group

# Create your models here.
class UserRole(models.Model):
    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE)
    role = models.ForeignKey(Group, on_delete=models.CASCADE)


