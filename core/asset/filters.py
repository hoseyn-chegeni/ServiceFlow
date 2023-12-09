import django_filters
from django_filters import FilterSet
from .models.asset import Asset
from .models.component import Component, ComponentCategory
from .models.consumable import Consumable
from .models.license import License, LicenseCategory


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
            'license_key',
            'software_name',
            'category',
            'product_key',
            'order_number',
        ]


class LicenseCategoryFilters(FilterSet):
        class Meta:
            model = LicenseCategory
            fields = [
                "id",
                "name",
            ]