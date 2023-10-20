from django.shortcuts import render
from django_filters.views import FilterView
from .filters import TaskFilter
from .models import Task

# Create your views here.

class TaskView(FilterView):
    model = Task
    filterset_class = TaskFilter
    paginate_by = 2
    context_object_name = 'task'
    template_name = 'tasks/tasks.html'
