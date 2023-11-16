from django.urls import path
from .views.asset import (
    AssetUpdateView,
    AssetListView,
    AssetDetailView,
    AssetDeleteView,
    AssetCreateView,
)

app_name = "asset"

urlpatterns = [
    # ASSET
    path("list/", AssetListView.as_view(), name="list"),
    path("create/", AssetCreateView.as_view(), name="create"),
    path("detail/<int:pk>", AssetDetailView.as_view(), name="detail"),
    path("update/<int:pk>", AssetUpdateView.as_view(), name="update"),
    path("delete/<int:pk>", AssetDeleteView.as_view(), name="delete"),
]
