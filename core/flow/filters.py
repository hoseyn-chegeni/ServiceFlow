import django_filters
from django_filters import FilterSet
from .models import WorkFlow, State


class FlowFilters(FilterSet):
    name = django_filters.CharFilter(lookup_expr="icontains")
    
    class Meta:
        model = WorkFlow
        fields = [
            "id",
            "name",
        ]


class StateFilters(FilterSet):
    state = django_filters.CharFilter(lookup_expr="icontains")
    
    class Meta:
        model = State
        fields = [
            "id",
            "state",
            "team",
        ]

