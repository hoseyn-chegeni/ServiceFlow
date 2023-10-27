from typing import Any
from django.db import models
from django.shortcuts import render
from django.urls import reverse_lazy
from django_filters.views import FilterView
from django.views.generic import DetailView, CreateView, DeleteView
from django.views.generic.edit import UpdateView
from .filters import MyCreatedMeetingsFilter, InvitedMeetingsFilter
from .models import Meetings
from .forms import CreateMeetingsForm
# Create your views here.
class InvitedMeetings(FilterView):
    model = Meetings
    filterset_class = InvitedMeetingsFilter
    template_name = 'meetings/invited_meetings.html'
    def get_queryset(self, **kwargs):
       qs = super().get_queryset(**kwargs)
       return qs.filter(attendees=self.request.user)
    
class MyCreatedMeetings(FilterView):
    model = Meetings
    filterset_class = MyCreatedMeetingsFilter
    template_name = 'meetings/my_created_meetings.html'
    def get_queryset(self, **kwargs):
       qs = super().get_queryset(**kwargs)
       return qs.filter(organizer_id=self.request.user.id)
    

class MeetingDetailView(DetailView):
    model = Meetings
    template_name = 'meetings/detail.html'

class CreateMeetingsView(CreateView):
    template_name = 'meetings/create.html'
    form_class = CreateMeetingsForm
    success_url = reverse_lazy('index:home')
    def form_valid(self, form):
        form.instance.organizer = self.request.user
        return super().form_valid(form)
    
class DeleteMeetings(DeleteView):
    model = Meetings
    success_url = reverse_lazy('index:home')

class UpdatedMeetings(UpdateView):
    model = Meetings
    fields = ("title","description", "date_time","duration","location", "attendees","action")
    success_url = reverse_lazy('index:home')
    template_name = 'meetings/update.html'
