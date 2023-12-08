from django.db import models
from accounts.models import User
from datetime import datetime, timedelta


# Create your models here.
def generate_pk():
    pass


class Reminder(models.Model):
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

    def delete_old_reminders():
        # Get current date and time
        now = datetime.now()
        # Calculate date and time 30 days ago
        a_days_ago = now - timedelta(days=1)
        # Delete reminders older than 30 days
        Reminder.objects.filter(created_at__lt=a_days_ago).delete()
