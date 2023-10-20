from django.urls import path
from .views import TaskView, MyTaskView

app_name = 'tasks'

urlpatterns = [
    path('',TaskView.as_view(), name='task_list'),
    path('mytask/',MyTaskView.as_view(), name='myTask_list'),
]