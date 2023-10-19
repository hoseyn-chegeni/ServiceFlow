from django.urls import path
from .views import IndexView, UserView


app_name = 'index'
urlpatterns = [
    path('',IndexView.as_view(), name='home'),
    path('users/',UserView.as_view(), name='users'),
]