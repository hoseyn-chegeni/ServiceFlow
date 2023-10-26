from django.urls import path
from .views import UserLogin, UserLogout

app_name = 'accounts'

urlpatterns = [
    path('login/', UserLogin.as_view(), name = 'login'),
    path('logout/',UserLogout.as_view(), name='logout')
]