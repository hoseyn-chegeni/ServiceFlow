from django.urls import path
from .views.user_role import AssignRoleToUser
from .views.role import (
    RoleListView,
    RoleCreateView,
    RoleDeleteView,
    RoleDetailView,
    RoleUpdateView,
)

app_name = "rbac"

urlpatterns = [
    # USER ROLE
    path(
        "assign_role_to_user/<int:pk>/",
        AssignRoleToUser.as_view(),
        name="assign_role_to_user",
    ),
    #  ROLE MANAGEMENT
    path("role_list/", RoleListView.as_view(), name="role_list"),
    path("role_create/", RoleCreateView.as_view(), name="role_create"),
    path("role_delete/<int:pk>/", RoleDeleteView.as_view(), name="role_delete"),
    path("role_detail/<int:pk>/", RoleDetailView.as_view(), name="role_detail"),
    path("role_update/<int:pk>/", RoleUpdateView.as_view(), name="role_update"),
]
