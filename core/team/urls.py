from django.urls import path
from .views import (
    TeamView,
    TeamCreateView,
    TeamDeleteView,
    TeamUpdateView,
    TeamDetailView,
)

app_name = "team"

urlpatterns = [
    path("", TeamView.as_view(), name="team_list"),
    path("create/", TeamCreateView.as_view(), name="create"),
    path("update/<int:pk>", TeamUpdateView.as_view(), name="update"),
    path("detail/<int:pk>", TeamDetailView.as_view(), name="detail"),
    path("delete/<int:pk>", TeamDeleteView.as_view(), name="delete"),
]
