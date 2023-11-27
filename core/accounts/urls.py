from django.urls import path, include
from .views import (
    UserLogin,
    UserLogout,
    CreateUser,
    UserView,
    UserUpdate,
    UserDetail,
    UserDelete,
    UserPasswordChangeView,
    SuspendUserView,
    ReactiveUserView,
    SuspendUserListView,
    UserActivitiesOnTasks,
    BulkUserImportView,
    CustomPasswordResetView,
    CustomPasswordResetDoneView,
    CustomPasswordResetConfirmView,
    CustomPasswordResetCompleteView,
)


app_name = "accounts"

urlpatterns = [
    path("api/", include("accounts.api.urls")),
    path("users/", UserView.as_view(), name="users"),
    path("login/", UserLogin.as_view(), name="login"),
    path("logout/", UserLogout.as_view(), name="logout"),
    path("create_user/", CreateUser.as_view(), name="create_user"),
    path("update/<int:pk>/", UserUpdate.as_view(), name="update"),
    path("detail/<int:pk>/", UserDetail.as_view(), name="detail"),
    path("delete/<int:pk>/", UserDelete.as_view(), name="delete"),
    path("change_password/", UserPasswordChangeView.as_view(), name="change_password"),
    path("suspend/<int:pk>/", SuspendUserView.as_view(), name="suspend"),
    path("reactive/<int:pk>/", ReactiveUserView.as_view(), name="reactive"),
    path("suspended/", SuspendUserListView.as_view(), name="suspended_list"),
    path(
        "task_activity/<int:pk>/", UserActivitiesOnTasks.as_view(), name="task_activity"
    ),
    path("user_bulk_upload/", BulkUserImportView.as_view(), name="user_bulk_upload"),
    # Password reset URLs
    path("password_reset/", CustomPasswordResetView.as_view(), name="password_reset"),
    path(
        "password_reset/done/",
        CustomPasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        CustomPasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/",
        CustomPasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
]
