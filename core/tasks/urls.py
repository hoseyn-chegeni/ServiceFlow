from django.urls import path
from .views import TaskView, MyTaskView,MyCreatedTaskView,CreateTaskView, TaskDetailView

app_name = 'tasks'

urlpatterns = [
    path('',TaskView.as_view(), name='task_list'),
    path('my_task/',MyTaskView.as_view(), name='myTask_list'),
    path('my_created_task/',MyCreatedTaskView.as_view(), name='myCreatedTask_list'),
    path('create_task/',CreateTaskView.as_view(), name='create_task'),
    path('detail/<int:pk>',TaskDetailView.as_view(), name='detail'),
]
