from django.urls import path
from .views import AssignRoleToUser

app_name = 'rbac'

urlpatterns = [
     path("assign_role_to_user/<int:pk>/", AssignRoleToUser.as_view(), name="assign_role_to_user"),
]