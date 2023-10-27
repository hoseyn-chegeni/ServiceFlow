from django.urls import path
from .views import MyCreatedMeetings, InvitedMeetings,MeetingDetailView

app_name = 'meetings'

urlpatterns = [
    path('invited_meetings/', InvitedMeetings.as_view(),name='invited_meetings'),
    path('my_created_meetings/', MyCreatedMeetings.as_view(),name='my_created_meetings'),
    path('detail/<int:pk>', MeetingDetailView.as_view(),name='detail'),
]