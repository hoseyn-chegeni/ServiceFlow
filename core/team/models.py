from django.db import models
from accounts.models import User
from django.contrib.auth.models import Group


# Create your models here.
def generate_pk():
    if Team.objects.last() is not None:
        number = (Team.objects.last().id) + 1
        return f"TEAM-{number}"
    else:
        return f"TEAM-1"


class Team(models.Model):
    team = models.CharField(
        default=generate_pk, max_length=255, unique=True, editable=False
    )
    name = models.CharField(max_length=255)
    access_group = models.OneToOneField(Group, on_delete=models.SET_NULL, blank=True,null=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    leader = models.ForeignKey(
        User, on_delete=models.SET_NULL, blank=True, null=True, related_name="leader"
    )
    # department
    responsibilities = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    # permissions
    # projects
    budget = models.IntegerField()
    created_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, blank=True, null=True
    )

    def __str__(self):
        return self.name
