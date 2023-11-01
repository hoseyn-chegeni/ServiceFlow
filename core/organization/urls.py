from django.urls import path

from .views import (
    OrganizationDeleteView,
    OrganizationCreateView,
    OrganizationListView,
    OrganizationUpdateView,
    OrganizationDetailView,
)


app_name = "organization"

urlpatterns = [
    path("list/", OrganizationListView.as_view(), name="list"),
    path("create/", OrganizationCreateView.as_view(), name="create"),
    path("detail/<int:pk>/", OrganizationDetailView.as_view(), name="detail"),
    path("update/<int:pk>/", OrganizationUpdateView.as_view(), name="update"),
    path("delete/<int:pk>/", OrganizationDeleteView.as_view(), name="delete"),
]
