import django_filters
from django_filters import FilterSet
from .models.asset import Asset
from .models.component import Component, ComponentCategory
from .models.consumable import Consumable, ConsumableCategory
from .models.license import License, LicenseCategory
from .models.asset_status import AssetStatus
from .models.asset_type import AssetType
from .models.accessory import Accessory, AccessoryCategory


class AssetFilters(FilterSet):
    name = django_filters.CharFilter(lookup_expr="icontains")
    assigned_user = django_filters.CharFilter(
        field_name="assigned_user__email",
    )

    class Meta:
        model = Asset
        fields = [
            "id",
            "name",
            "manufacturer",
            "location",
            "assigned_user",
            "status",
        ]


class ComponentFilters(FilterSet):
    company = django_filters.CharFilter(lookup_expr="icontains")
    name = django_filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = Component
        fields = [
            "company",
            "name",
            "serial",
            "category",
            "supplier",
            "location",
            "order_number",
        ]


class ComponentCategoryFilters(FilterSet):
    name = django_filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = ComponentCategory
        fields = [
            "id",
            "name",
        ]


class ConsumableFilters(FilterSet):
    name = django_filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = Consumable
        fields = [
            "id",
            "name",
            "category",
            "location",
            "order_number",
        ]


class LicenseFilters(FilterSet):
    class Meta:
        model = License
        fields = [
            "license_key",
            "software_name",
            "category",
            "product_key",
            "order_number",
        ]


class LicenseCategoryFilters(FilterSet):
    class Meta:
        model = LicenseCategory
        fields = [
            "id",
            "name",
        ]


class AssetStatusFilters(FilterSet):
    class Meta:
        model = AssetStatus
        fields = [
            "id",
            "name",
        ]


class AssetTypeFilters(FilterSet):
    class Meta:
        model = AssetType
        fields = [
            "id",
            "name",
        ]


class AccessoryFilters(FilterSet):
    class Meta:
        model = Accessory
        fields = [
            "id",
            "name",
            "category",
            "order_number",
            "location",
        ]


class AccessoryCategoryFilters(FilterSet):
    name = django_filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = AccessoryCategory
        fields = [
            "id",
            "name",
        ]


class ConsumableCategoryFilters(FilterSet):
    name = django_filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = ConsumableCategory
        fields = [
            "id",
            "name",
        ]
