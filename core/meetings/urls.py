from django.urls import path
from .views import MyCreatedMeetings, InvitedMeetings

app_name = 'meetings'

urlpatterns = [
    path('invited_meetings/', InvitedMeetings.as_view(),name='invited_meetings'),
    path('my_created_meetings/', MyCreatedMeetings.as_view(),name='my_created_meetings'),
]