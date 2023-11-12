from django.urls import path
from .views.task import (
    TaskView,
    MyTaskView,
    MyCreatedTaskView,
    CreateTaskView,
    TaskDetailView,
    TaskDelete,
    TaskUpdate,
    MyTeamTasks,
)
from .views.assignee import (
    TaskAssignmentLogsView,
    TaskAssignTo,
    TaskAssignToMe,
)
from .views.comment import TaskCommentView
from .views.status import StatusCreateView,StatusDeleteView,StatusDetailView,StatusListView,StatusUpdateView
from .views.type import TypeCreateView,TypeDeleteView, TypeDetailView,TypeListView,TypeUpdateView
app_name = "tasks"

urlpatterns = [
    #Task
    path("", TaskView.as_view(), name="task_list"),
    path("my_task/", MyTaskView.as_view(), name="myTask_list"),
    path("my_created_task/", MyCreatedTaskView.as_view(), name="myCreatedTask_list"),
    path("create_task/", CreateTaskView.as_view(), name="create_task"),
    path("detail/<int:pk>", TaskDetailView.as_view(), name="detail"),
    path("delete/<int:pk>", TaskDelete.as_view(), name="delete"),
    path("update/<int:pk>", TaskUpdate.as_view(), name="update"),
    #ASSIGNEE
    path("tasks_assigned_to_my_team/", MyTeamTasks.as_view(), name="my_team"),
    path("assign_to_me/<int:pk>/", TaskAssignToMe.as_view(), name="assign_to_me"),
    path("assign_to/<int:pk>/", TaskAssignTo.as_view(), name="assign_to"),
    path("assign_log/<int:pk>/", TaskAssignmentLogsView.as_view(), name="assign_log"),
    #COMMENT
    path("comment/<int:pk>/", TaskCommentView.as_view(), name="task_comment"),
    #STATUS
    path("list_status/", StatusListView.as_view(), name="list_status"),
    path("create_status/", StatusCreateView.as_view(), name="create_status"),
    path("detail_status/<int:pk>/", StatusDetailView.as_view(), name="detail_status"),
    path("delete_status/<int:pk>/", StatusDeleteView.as_view(), name="delete_status"),
    path("update_status/<int:pk>/", StatusUpdateView.as_view(), name="update_status"),
    #TYPE
    path("list_type/", TypeListView.as_view(), name="list_type"),
    path("create_type/", TypeCreateView.as_view(), name="create_type"),
    path("detail_type/<int:pk>/", TypeDetailView.as_view(), name="detail_type"),
    path("delete_type/<int:pk>/", TypeDeleteView.as_view(), name="delete_type"),
    path("update_type/<int:pk>/", TypeUpdateView.as_view(), name="update_type"),
]
