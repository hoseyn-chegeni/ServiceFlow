from typing import Any
from django_filters.views import FilterView
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
)
from .filters import TaskFilter
from .models import Task
from .forms import CreateTaskForm
from django.urls import reverse_lazy

# Create your views here.


class TaskView(FilterView):
    model = Task
    filterset_class = TaskFilter
    paginate_by = 2
    context_object_name = "task"
    template_name = "tasks/tasks.html"



class MyTaskView(ListView):

    model = Task
    context_object_name = "tasks"
    template_name = "tasks/myTask.html"
    
    def get_queryset(self, **kwargs):
        qs = super().get_queryset(**kwargs)
        return qs.filter(assign_to_id=self.request.user.id)
    


class MyCreatedTaskView(ListView):
    template_name = "tasks/myCreatedTask.html"
    model = Task
    context_object_name = "tasks"

    def get_queryset(self, **kwargs):
        qs = super().get_queryset(**kwargs)
        return qs.filter(creator_id=self.request.user.id)


class CreateTaskView(CreateView):
    template_name = "tasks/create_task.html"
    form_class = CreateTaskForm
    success_url = reverse_lazy("index:home")

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


class TaskDetailView(DetailView):
    model = Task
    template_name = "tasks/detail.html"


class TaskUpdate(UpdateView):
    model = Task
    fields = ("title", "description", "type", "status")
    template_name = "tasks/update.html"
    success_url = reverse_lazy("tasks:task_list")


class TaskDelete(DeleteView):
    model = Task
    template_name = "tasks/delete.html"
    success_url = reverse_lazy("tasks:task_list")


class MyTeamTasks(ListView):
    model = Task
    template_name = "tasks/my_team_tasks.html"
    context_object_name = "tasks"

    def get_queryset(self, **kwargs):
        qs = super().get_queryset(**kwargs)
        return qs.filter(type__assigned_to=self.request.user.member_of)


class TaskAssignToMe(UpdateView):
    template_name = "tasks/assign_to_me.html"
    success_url = reverse_lazy("tasks:my_team")
    model = Task
    fields = ("assign_to",)

    def form_valid(self, form):
        form.instance.assign_to = self.request.user
        return super().form_valid(form)
