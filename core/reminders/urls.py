from django.urls import path
from . views import MyCreatedReminder

app_name = 'reminders'

urlpatterns = [
    path('my_created_reminder/', MyCreatedReminder.as_view(), name='my_created_reminders')
]