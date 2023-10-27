from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django_filters.views import FilterView
from django.views.generic import ListView, CreateView, DetailView
from .filters import TaskFilter
from .models import Task
from  .forms import CreateTaskForm
from django.urls import reverse_lazy

# Create your views here.

class TaskView(FilterView):
    model = Task
    filterset_class = TaskFilter
    paginate_by = 2
    context_object_name = 'task'
    template_name = 'tasks/tasks.html'


class MyTaskView(ListView):
    template_name = 'tasks/myCreatedTask.html'
    model = Task
    context_object_name = 'tasks'
    def get_queryset(self, **kwargs):
       qs = super().get_queryset(**kwargs)
       return qs.filter(assign_to_id=self.request.user.id)


class MyCreatedTaskView(ListView):
    template_name = 'tasks/myTask.html'
    model = Task
    context_object_name = 'tasks'
    def get_queryset(self, **kwargs):
       qs = super().get_queryset(**kwargs)
       return qs.filter(creator_id=self.request.user.id)
    

class CreateTaskView(CreateView):
    template_name = 'tasks/create_task.html'
    form_class = CreateTaskForm
    success_url = reverse_lazy('index:home')
    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)
    
class TaskDetailView(DetailView):
    model = Task
    template_name = 'tasks/detail.html'