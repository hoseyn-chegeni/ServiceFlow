from django.urls import path
from .views import MyCreatedReminder, AssignedReminder

app_name = "reminders"

urlpatterns = [
    path(
        "my_created_reminder/", MyCreatedReminder.as_view(), name="my_created_reminders"
    ),
    path("assigned_reminder/", AssignedReminder.as_view(), name="assigned_reminder"),
]
