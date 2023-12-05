import django_filters
from django_filters import FilterSet
from .models import TaskLog

class TaskLogFilter(FilterSet):
    title = django_filters.CharFilter(lookup_expr="icontains")
    user = django_filters.CharFilter(field_name='user__email',)
    task_id =  django_filters.CharFilter(field_name='task__id',)
    task_title =  django_filters.CharFilter(lookup_expr="icontains", field_name='task__title',)


    class Meta:
        model = TaskLog
        fields = [
            "id",
            "user",
            "task_id",
            "task_title",
            "event_type",
        ]