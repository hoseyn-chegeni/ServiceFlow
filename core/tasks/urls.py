from django.urls import path
from .views import (
    TaskView,
    MyTaskView,
    MyCreatedTaskView,
    CreateTaskView,
    TaskDetailView,
    TaskDelete,
    TaskUpdate,
    MyTeamTasks,
    TaskAssignToMe,
    TaskAssignToMe_v2,
)

app_name = "tasks"

urlpatterns = [
    path("", TaskView.as_view(), name="task_list"),
    path("my_task/", MyTaskView.as_view(), name="myTask_list"),
    path("my_created_task/", MyCreatedTaskView.as_view(), name="myCreatedTask_list"),
    path("create_task/", CreateTaskView.as_view(), name="create_task"),
    path("detail/<int:pk>", TaskDetailView.as_view(), name="detail"),
    path("delete/<int:pk>", TaskDelete.as_view(), name="delete"),
    path("update/<int:pk>", TaskUpdate.as_view(), name="update"),
    path("tasks_assigned_to_my_team/", MyTeamTasks.as_view(), name="my_team"),
    path("assign_to_me/<int:pk>/", TaskAssignToMe.as_view(), name="assign_to_me"),
    path("assign_to_me_2/<int:pk>/", TaskAssignToMe_v2.as_view(), name="assign_to_me_2"),

]
