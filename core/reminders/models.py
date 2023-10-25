from django.db import models
from accounts.models import User
# Create your models here.
def generate_pk():
    number = (Reminder.objects.all().count())+1
    return f'NOTE-{number}'

class Reminder (models.Model):
    reminder= models.CharField(default=generate_pk,max_length=255, unique= True, editable=False, verbose_name='Reminder ID')
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_by')
    assign_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Assign_to')
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)

    def __str__(self):
        return self.reminder