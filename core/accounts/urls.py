from django.urls import path
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
)

app_name = "accounts"

urlpatterns = [
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
]
