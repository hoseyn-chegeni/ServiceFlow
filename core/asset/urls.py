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
from .views.asset_condition import (
    AssetConditionCreateView,
    AssetConditionDeleteView,
    AssetConditionDetailView,
    AssetConditionListView,
    AssetConditionUpdateView,
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
    # ASSET CONDITION
    path("condition_list/", AssetConditionListView.as_view(), name="condition_list"),
    path(
        "condition_create/", AssetConditionCreateView.as_view(), name="condition_create"
    ),
    path(
        "condition_detail/<int:pk>",
        AssetConditionDetailView.as_view(),
        name="condition_detail",
    ),
    path(
        "condition_update/<int:pk>",
        AssetConditionUpdateView.as_view(),
        name="condition_update",
    ),
    path(
        "condition_delete/<int:pk>",
        AssetConditionDeleteView.as_view(),
        name="condition_delete",
    ),
]
