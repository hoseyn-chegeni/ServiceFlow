from django.urls import path
from .views import TaskView

app_name = 'tasks'

urlpatterns = [
    path('',TaskView.as_view(), name='task_list'),
]