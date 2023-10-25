import django_filters
from django_filters import FilterSet
from . models import Team


class TeamFilter(FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Team
        fields = ['id','name','leader',]