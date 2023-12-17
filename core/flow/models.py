from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
class WorkFlow(models.Model):
    name = models.CharField(max_length = 255, unique = True)
    root = models.OneToOneField('State',on_delete = models.CASCADE)
    diagram = models.ImageField(upload_to="images", blank= True, null = True)
    created_by = models.ForeignKey("accounts.User", on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class State(models.Model):
    state = models.CharField(max_length = 255, )
    team  = models.ForeignKey('team.Team', on_delete = models.CASCADE, blank = True, null = True)
    process_percentage = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    action = models.ManyToManyField('Action',blank = True)

    def __str__(self):
        return self.state
    
class Action(models.Model):
    title = models.CharField(max_length = 255)
    next_state = models.ForeignKey('State',on_delete = models.SET_NULL, blank = True, null = True, related_name = 'next')

    def __str__(self):
        return self.title
    