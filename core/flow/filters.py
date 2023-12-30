import django_filters
from django_filters import FilterSet
from .models import WorkFlow


class FlowFilters(FilterSet):
    name = django_filters.CharFilter(lookup_expr="icontains")
    
    class Meta:
        model = WorkFlow
        fields = [
            "id",
            "name",
        ]