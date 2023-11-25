import django_filters
from django_filters import FilterSet
from .models.asset import Asset


class AssetFilters(FilterSet):
    name = django_filters.CharFilter(lookup_expr="icontains")

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
