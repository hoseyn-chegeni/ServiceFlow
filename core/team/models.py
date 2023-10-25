from django.db import models
from accounts.models import User
# Create your models here.
def generate_pk():
    number = (Team.objects.all().count())+1
    return f'TEAM-{number}'

class Team (models.Model):
    team= models.CharField(default=generate_pk,max_length=255, unique= True, editable=False)
    name = models.CharField(max_length=255)
    description  = models.TextField()
    members  = models.ManyToManyField(User, related_name='members')
    created_at  = models.DateTimeField(auto_now_add= True)
    updated_at  = models.DateTimeField(auto_now= True)
    leader  = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null= True, related_name='leader')
    # department
    responsibilities = models.TextField(blank=True, null= True)
    is_active  = models.BooleanField(default=True)
    # permissions
    # projects
    budget  = models.IntegerField()

    def __str__(self):
        return self.team