import django_filters
from django_filters import FilterSet
from .models import Department


class DepartmentFilters(FilterSet):
    name = django_filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = Department
        fields = [
            "id",
            "name",
            "manager",
            "active_status",
            "organization",
        ]
