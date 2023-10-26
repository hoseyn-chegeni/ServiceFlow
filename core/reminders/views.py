from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView
from .models import Reminder
# Create your views here.

class MyCreatedReminder(ListView):
    template_name = 'reminder/my_created_reminder.html'
    model = Reminder
    context_object_name = 'reminders'
    def get_queryset(self, **kwargs):
       qs = super().get_queryset(**kwargs)
       return qs.filter(created_by_id=self.request.user.id)
    

class AssignedReminder(ListView):
    template_name = 'reminder/assigned_reminder.html'
    model = Reminder
    context_object_name = 'reminder'
    def get_queryset(self):
        user = self.request.user
        return Reminder.objects.filter(assign_to = user)