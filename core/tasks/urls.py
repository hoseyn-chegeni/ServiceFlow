from django.urls import path
from .views import TaskView, MyTaskView,MyCreatedTaskView

app_name = 'tasks'

urlpatterns = [
    path('',TaskView.as_view(), name='task_list'),
    path('mytask/',MyTaskView.as_view(), name='myTask_list'),
    path('my_created_task/',MyCreatedTaskView.as_view(), name='myCreatedTask_list'),
]