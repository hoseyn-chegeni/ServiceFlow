from django.db import models
from accounts.models import User

# Create your models here.


class DatabaseLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    event_type = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    table_name = models.CharField(max_length=255)
    record_id = models.PositiveIntegerField()
    field_name = models.CharField(max_length=255)
    additional_info = models.TextField(blank=True, null=True)
    is_success = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.event_type} on {self.table_name} at {self.timestamp}"


class TaskLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name = 'user')
    task = models.ForeignKey(
        "tasks.Task",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="log",
    )
    event_type = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    additional_info = models.TextField(blank=True, null=True)
    is_success = models.BooleanField(default=True)

    def __str__(self):
        return self.additional_info


class UserAuthenticationLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    login_time = models.DateTimeField(auto_now_add=True)
    ip_address = models.CharField(max_length=50)
    status = models.CharField(max_length=20) 