from django.urls import path
from .views.asset import (
    AssetUpdateView,
    AssetListView,
    AssetDetailView,
    AssetDeleteView,
    AssetCreateView,
)
from .views.asset_status import AssetStatusCreateView, AssetStatusDeleteView,AssetStatusDetailView,AssetStatusListView,AssetStatusUpdateView

app_name = "asset"

urlpatterns = [
    # ASSET
    path("list/", AssetListView.as_view(), name="list"),
    path("create/", AssetCreateView.as_view(), name="create"),
    path("detail/<int:pk>", AssetDetailView.as_view(), name="detail"),
    path("update/<int:pk>", AssetUpdateView.as_view(), name="update"),
    path("delete/<int:pk>", AssetDeleteView.as_view(), name="delete"),
    #ASSET STATUS
    path("status_list/", AssetStatusListView.as_view(), name="status_list"),
    path("status_create/", AssetStatusCreateView.as_view(), name="status_create"),
    path("status_detail/<int:pk>", AssetStatusDetailView.as_view(), name="status_detail"),
    path("status_update/<int:pk>", AssetStatusUpdateView.as_view(), name="status_update"),
    path("status_delete/<int:pk>", AssetStatusDeleteView.as_view(), name="status_delete"),
]