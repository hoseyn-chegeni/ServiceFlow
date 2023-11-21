from django.db import models
from django.contrib.auth.models import Permission


# Create your models here.
class Role(models.Model):
    name = models.CharField(max_length = 255, )
    permissions = models.ManyToManyField(Permission)
    created_by = models.ForeignKey('accounts.User', on_delete = models.SET_NULL, blank = True, null = True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    is_active = models.BooleanField(default = True)

    def __str__(self):
        return self.name


class UserRole(models.Model):
    user = models.ForeignKey('accounts.User', on_delete = models.CASCADE)
    role = models.ForeignKey(Role, on_delete = models.CASCADE)