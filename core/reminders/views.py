from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DeleteView,
    DetailView,
    CreateView,
    UpdateView,
)
from .models import Reminder
from .forms import ReminderCreateForm
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class MyCreatedReminder(LoginRequiredMixin, ListView):
    template_name = "reminder/my_created_reminder.html"
    model = Reminder
    context_object_name = "reminders"

    def get_queryset(self, **kwargs):
        qs = super().get_queryset(**kwargs)
        return qs.filter(created_by_id=self.request.user.id)


class AssignedReminder(LoginRequiredMixin, ListView):
    template_name = "reminder/assigned_reminder.html"
    model = Reminder
    context_object_name = "reminder"

    def get_queryset(self):
        user = self.request.user
        return Reminder.objects.filter(assign_to=user)


class ReminderDetailView(LoginRequiredMixin, DetailView):
    model = Reminder
    template_name = "reminder/detail.html"


class ReminderUpdateView(LoginRequiredMixin, UpdateView):
    model = Reminder
    template_name = "reminder/update.html"
    fields = ("title", "description", "date", "time", "assign_to", "is_completed")
    success_url = reverse_lazy("reminders:my_created_reminders")


class ReminderCreateView(LoginRequiredMixin, CreateView):
    model = Reminder
    template_name = "reminder/create.html"
    form_class = ReminderCreateForm
    success_url = reverse_lazy("reminders:my_created_reminders")

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class ReminderDeleteView(LoginRequiredMixin, DeleteView):
    model = Reminder
    template_name = "reminder/delete.html"
    success_url = reverse_lazy("reminders:my_created_reminders")
