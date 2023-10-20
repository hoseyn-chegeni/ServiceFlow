import django_filters
from django_filters import FilterSet
from . models import TASK


class TaskFilter(FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    task = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = TASK
        fields = ['task','title','creator', 'type', 'status', 'assign_to',]