from django.db import models
from accounts.models import User


# Create your models here.
def generate_pk():
    if Reminder.objects.last() is not None:
        number = (Reminder.objects.last().id) + 1
        return f"REMINDER-{number}"
    else:
        return f"REMINDER-1"


class Reminder(models.Model):
    reminder = models.CharField(
        default=generate_pk,
        max_length=255,
        unique=True,
        editable=False,
        verbose_name="Reminder ID",
    )
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="created_by"
    )
    assign_to = models.ManyToManyField(User)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.reminder
