from django.urls import path
from .views import (
    MyCreatedReminder,
    AssignedReminder,
    ReminderCreateView,
    ReminderDeleteView,
    ReminderDetailView,
    ReminderUpdateView,
)

app_name = "reminders"

urlpatterns = [
    path(
        "my_created_reminder/", MyCreatedReminder.as_view(), name="my_created_reminders"
    ),
    path("assigned_reminder/", AssignedReminder.as_view(), name="assigned_reminder"),
    path("create/", ReminderCreateView.as_view(), name="create"),
    path("update/<int:pk>", ReminderUpdateView.as_view(), name="update"),
    path("detail/<int:pk>", ReminderDetailView.as_view(), name="detail"),
    path("delete/<int:pk>", ReminderDeleteView.as_view(), name="delete"),
]
