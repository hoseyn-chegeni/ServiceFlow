from django.urls import path
from .views.asset import (
    AssetUpdateView,
    AssetListView,
    AssetDetailView,
    AssetDeleteView,
    AssetCreateView,
)
from .views.asset_status import (
    AssetStatusCreateView,
    AssetStatusDeleteView,
    AssetStatusDetailView,
    AssetStatusListView,
    AssetStatusUpdateView,
)

from .views.asset_type import (
    AssetTypeCreateView,
    AssetTypeDeleteView,
    AssetTypeDetailView,
    AssetTypeListView,
    AssetTypeUpdateView,
)
from .views.component import (
    ComponentCreateView,
    ComponentDeleteView,
    ComponentDetailView,
    ComponentListView,
    ComponentUpdateView,
)

app_name = "asset"

urlpatterns = [
    # ASSET
    path("list/", AssetListView.as_view(), name="list"),
    path("create/", AssetCreateView.as_view(), name="create"),
    path("detail/<int:pk>", AssetDetailView.as_view(), name="detail"),
    path("update/<int:pk>", AssetUpdateView.as_view(), name="update"),
    path("delete/<int:pk>", AssetDeleteView.as_view(), name="delete"),
    # ASSET STATUS
    path("status_list/", AssetStatusListView.as_view(), name="status_list"),
    path("status_create/", AssetStatusCreateView.as_view(), name="status_create"),
    path(
        "status_detail/<int:pk>", AssetStatusDetailView.as_view(), name="status_detail"
    ),
    path(
        "status_update/<int:pk>", AssetStatusUpdateView.as_view(), name="status_update"
    ),
    path(
        "status_delete/<int:pk>", AssetStatusDeleteView.as_view(), name="status_delete"
    ),
    # ASSET TYPE
    path("type_list/", AssetTypeListView.as_view(), name="type_list"),
    path("type_create/", AssetTypeCreateView.as_view(), name="type_create"),
    path("type_detail/<int:pk>", AssetTypeDetailView.as_view(), name="type_detail"),
    path("type_update/<int:pk>", AssetTypeUpdateView.as_view(), name="type_update"),
    path("type_delete/<int:pk>", AssetTypeDeleteView.as_view(), name="type_delete"),

    # COMPONENT
    path("component_list/", ComponentListView.as_view(), name="component_list"),
    path("component_create/", ComponentCreateView.as_view(), name="component_create"),
    path("component_detail/<int:pk>", ComponentDetailView.as_view(), name="component_detail"),
    path("component_update/<int:pk>", ComponentUpdateView.as_view(), name="component_update"),
    path("component_delete/<int:pk>", ComponentDeleteView.as_view(), name="component_delete"),
]
