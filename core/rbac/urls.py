from django.urls import path
from .views.user_role import (
    AssignRoleToUser,
    UserRolesListView,
    UserRoleDeleteFromProfile,
    UserRoleDeleteFromRoleDetail,
)
from .views.role import (
    RoleListView,
    RoleCreateView,
    RoleDeleteView,
    RoleDetailView,
    RoleUpdateView,
)
from .views.permissions import PermissionListView, PermissionDetailView

app_name = "rbac"

urlpatterns = [
    # USER ROLE
    path(
        "assign_role_to_user/<int:pk>/",
        AssignRoleToUser.as_view(),
        name="assign_role_to_user",
    ),
    path("user_role_list/", UserRolesListView.as_view(), name="user_role_list"),
    path(
        "user_role_delete_from_profile/<int:pk>/",
        UserRoleDeleteFromProfile.as_view(),
        name="user_role_delete_from_profile",
    ),
    path(
        "user_role_delete_from_role_detail/<int:pk>/",
        UserRoleDeleteFromRoleDetail.as_view(),
        name="user_role_delete_from_role_detail",
    ),
    #  ROLE MANAGEMENT
    path("role_list/", RoleListView.as_view(), name="role_list"),
    path("role_create/", RoleCreateView.as_view(), name="role_create"),
    path("role_delete/<int:pk>/", RoleDeleteView.as_view(), name="role_delete"),
    path("role_detail/<int:pk>/", RoleDetailView.as_view(), name="role_detail"),
    path("role_update/<int:pk>/", RoleUpdateView.as_view(), name="role_update"),
    # PERMISSION
    path("permission_list/", PermissionListView.as_view(), name="permission_list"),
    path(
        "permission_detail/<int:pk>/",
        PermissionDetailView.as_view(),
        name="permission_detail",
    ),
]
