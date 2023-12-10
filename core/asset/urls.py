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
    AllBYODListView,
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
    ComponentCategoryCreateView,
    ComponentCategoryDeleteView,
    ComponentCategoryDetailView,
    ComponentCategoryListView,
    ComponentCategoryUpdateView,
)

from .views.license import (
    LicenseCreateView,
    LicenseDeleteView,
    LicenseDetailView,
    LicenseListView,
    LicenseUpdateView,
    LicenseCategoryDeleteView,
    LicenseCategoryCreateView,
    LicenseCategoryDetailView,
    LicenseCategoryListView,
    LicenseCategoryUpdateView,
)


from .views.consumable import (
    ConsumableCreateView,
    ConsumableDeleteView,
    ConsumableDetailView,
    ConsumableListView,
    ConsumableUpdateView,
    ConsumableCategoryCreateView,
    ConsumableCategoryDeleteView,
    ConsumableCategoryDetailView,
    ConsumableCategoryListView,
    ConsumableCategoryUpdateView,
)

from .views.accessory import (
    AccessoryCreateView,
    AccessoryDeleteView,
    AccessoryDetailView,
    AccessoryListView,
    AccessoryUpdateView,
    AccessoryCategoryCreateView,
    AccessoryCategoryDeleteView,
    AccessoryCategoryDetailView,
    AccessoryCategoryListView,
    AccessoryCategoryUpdateView,
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
    path("BYOD", AllBYODListView.as_view(), name="BYOD"),
    # ASSET TYPE
    path("type_list/", AssetTypeListView.as_view(), name="type_list"),
    path("type_create/", AssetTypeCreateView.as_view(), name="type_create"),
    path("type_detail/<int:pk>", AssetTypeDetailView.as_view(), name="type_detail"),
    path("type_update/<int:pk>", AssetTypeUpdateView.as_view(), name="type_update"),
    path("type_delete/<int:pk>", AssetTypeDeleteView.as_view(), name="type_delete"),
    # COMPONENT
    path("component_list/", ComponentListView.as_view(), name="component_list"),
    path("component_create/", ComponentCreateView.as_view(), name="component_create"),
    path(
        "component_detail/<int:pk>",
        ComponentDetailView.as_view(),
        name="component_detail",
    ),
    path(
        "component_update/<int:pk>",
        ComponentUpdateView.as_view(),
        name="component_update",
    ),
    path(
        "component_delete/<int:pk>",
        ComponentDeleteView.as_view(),
        name="component_delete",
    ),
    # COMPONENT CATEGORY
    path(
        "component_category_list/",
        ComponentCategoryListView.as_view(),
        name="component_category_list",
    ),
    path(
        "component_category_create/",
        ComponentCategoryCreateView.as_view(),
        name="component_category_create",
    ),
    path(
        "component_category_detail/<int:pk>",
        ComponentCategoryDetailView.as_view(),
        name="component_category_detail",
    ),
    path(
        "component_category_update/<int:pk>",
        ComponentCategoryUpdateView.as_view(),
        name="component_category_update",
    ),
    path(
        "component_category_delete/<int:pk>",
        ComponentCategoryDeleteView.as_view(),
        name="component_category_delete",
    ),
    # LICENSE
    path("license_list/", LicenseListView.as_view(), name="license_list"),
    path("license_create/", LicenseCreateView.as_view(), name="license_create"),
    path(
        "license_detail/<int:pk>",
        LicenseDetailView.as_view(),
        name="license_detail",
    ),
    path(
        "license_update/<int:pk>",
        LicenseUpdateView.as_view(),
        name="license_update",
    ),
    path(
        "license_delete/<int:pk>",
        LicenseDeleteView.as_view(),
        name="license_delete",
    ),
    # LICENSE CATEGORY
    path(
        "license_category_list/",
        LicenseCategoryListView.as_view(),
        name="license_category_list",
    ),
    path(
        "license_category_create/",
        LicenseCategoryCreateView.as_view(),
        name="license_category_create",
    ),
    path(
        "license_category_detail/<int:pk>",
        LicenseCategoryDetailView.as_view(),
        name="license_category_detail",
    ),
    path(
        "license_category_update/<int:pk>",
        LicenseCategoryUpdateView.as_view(),
        name="license_category_update",
    ),
    path(
        "license_category_delete/<int:pk>",
        LicenseCategoryDeleteView.as_view(),
        name="license_category_delete",
    ),
    # CONSUMABLE
    path("consumable_list/", ConsumableListView.as_view(), name="consumable_list"),
    path(
        "consumable_create/", ConsumableCreateView.as_view(), name="consumable_create"
    ),
    path(
        "consumable_detail/<int:pk>",
        ConsumableDetailView.as_view(),
        name="consumable_detail",
    ),
    path(
        "consumable_update/<int:pk>",
        ConsumableUpdateView.as_view(),
        name="consumable_update",
    ),
    path(
        "consumable_delete/<int:pk>",
        ConsumableDeleteView.as_view(),
        name="consumable_delete",
    ),
    # CONSUMABLE CATEGORY
    path(
        "consumable_category_list/",
        ConsumableCategoryListView.as_view(),
        name="consumable_category_list",
    ),
    path(
        "consumable_category_create/",
        ConsumableCategoryCreateView.as_view(),
        name="consumable_category_create",
    ),
    path(
        "consumable_category_detail/<int:pk>",
        ConsumableCategoryDetailView.as_view(),
        name="consumable_category_detail",
    ),
    path(
        "consumable_category_update/<int:pk>",
        ConsumableCategoryUpdateView.as_view(),
        name="consumable_category_update",
    ),
    path(
        "consumable_category_delete/<int:pk>",
        ConsumableCategoryDeleteView.as_view(),
        name="consumable_category_delete",
    ),
    # ACCESSORY
    path("accessory_list/", AccessoryListView.as_view(), name="accessory_list"),
    path("accessory_create/", AccessoryCreateView.as_view(), name="accessory_create"),
    path(
        "accessory_detail/<int:pk>",
        AccessoryDetailView.as_view(),
        name="accessory_detail",
    ),
    path(
        "accessory_update/<int:pk>",
        AccessoryUpdateView.as_view(),
        name="accessory_update",
    ),
    path(
        "accessory_delete/<int:pk>",
        AccessoryDeleteView.as_view(),
        name="accessory_delete",
    ),
    # ACCESSORY-CATEGORY
    path(
        "accessory_category_list/",
        AccessoryCategoryListView.as_view(),
        name="accessory_category_list",
    ),
    path(
        "accessory_category_create/",
        AccessoryCategoryCreateView.as_view(),
        name="accessory_category_create",
    ),
    path(
        "accessory_category_detail/<int:pk>",
        AccessoryCategoryDetailView.as_view(),
        name="accessory_category_detail",
    ),
    path(
        "accessory_category_update/<int:pk>",
        AccessoryCategoryUpdateView.as_view(),
        name="accessory_category_update",
    ),
    path(
        "accessory_category_delete/<int:pk>",
        AccessoryCategoryDeleteView.as_view(),
        name="accessory_category_delete",
    ),
]
