from django.urls import path
from .views import UserLogin, UserLogout,CreateUser,UserView

app_name = 'accounts'

urlpatterns = [
    path('users/',UserView.as_view(), name='users'),
    path('login/', UserLogin.as_view(), name = 'login'),
    path('logout/',UserLogout.as_view(), name='logout'),
    path('create_user/',CreateUser.as_view(), name='create_user'),
]