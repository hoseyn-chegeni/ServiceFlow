import django_filters
from django_filters import FilterSet
from . models import Task


class TaskFilter(FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Task
        fields = ['id','title','creator', 'type', 'status', 'assign_to',]