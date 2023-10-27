from django.db import models
from accounts.models import User
# Create your models here.
def generate_pk():
    number = (Meetings.objects.all().count())+1
    return f'MEET-{number}'

class Meetings (models.Model):
    meeting= models.CharField(default=generate_pk,max_length=255, unique= True, editable=False)  
    title = models.CharField(max_length=255)
    description = models.TextField()
    date_time = models.DateTimeField()
    duration = models.IntegerField()
    location = models.CharField(max_length=255)  #After add location model it must be a relation
    attendees = models.ManyToManyField(User, related_name='attendees')
    # reminder = 0
    organizer = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='organizer')
    status = models.ForeignKey('MeetingStatus', on_delete=models.SET_NULL, blank=True, null=True)
    action =  models.TextField()

    def __str__(self):
        return f'{self.meeting}{self.title}'

class MeetingStatus(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name