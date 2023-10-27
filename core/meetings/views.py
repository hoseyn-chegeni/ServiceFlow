from django.shortcuts import render
from django_filters.views import FilterView
from .filters import MyCreatedMeetingsFilter, InvitedMeetingsFilter
from .models import Meetings
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