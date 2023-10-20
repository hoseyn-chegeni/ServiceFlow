from django.urls import path
from .views import UserLogin

app_name = 'accounts'

urlpatterns = [
    path('login/', UserLogin.as_view(), name = 'login')
]