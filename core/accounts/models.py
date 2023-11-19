from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class User(AbstractUser):
    username = None
    email = models.EmailField(_("email address"), unique=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    member_of = models.ForeignKey(
        "team.Team",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="member",
    )
    image = models.ImageField(upload_to="images", default="images/default.jpeg")
    login_attempts = models.IntegerField(default=0)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
