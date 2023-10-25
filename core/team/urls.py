from django.urls import path
from .views import TeamView

app_name = 'team'

urlpatterns = [
    path('',TeamView.as_view(), name='team_list')
]