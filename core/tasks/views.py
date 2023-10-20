from django.db.models.query import QuerySet
from django.shortcuts import render
from django_filters.views import FilterView
from django.views.generic import ListView
from .filters import TaskFilter
from .models import Task

# Create your views here.

class TaskView(FilterView):
    model = Task
    filterset_class = TaskFilter
    paginate_by = 2
    context_object_name = 'task'
    template_name = 'tasks/tasks.html'


class MyTaskView(ListView):
    template_name = 'tasks/myTask.html'
    model = Task
    context_object_name = 'tasks'
    def get_queryset(self, **kwargs):
       qs = super().get_queryset(**kwargs)
       return qs.filter(assign_to_id=self.request.user.id)
