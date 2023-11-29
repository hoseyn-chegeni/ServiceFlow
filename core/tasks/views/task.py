from django.shortcuts import get_object_or_404
from django_filters.views import FilterView
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
)
from ..filters import TaskFilter
from ..models import Task
from ..forms import CreateTaskForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from db_events.models import TaskLog


class TaskView(LoginRequiredMixin, FilterView):
    model = Task
    filterset_class = TaskFilter
    context_object_name = "tasks"
    template_name = "tasks/tasks.html"

    def get_paginate_by(self, queryset):
        # Get the value for paginate_by dynamically (e.g., from a form input or session)
        # Example: Set paginate_by to a user-selected value stored in session
        user_selected_value = self.request.session.get(
            "items_per_page", 10
        )  # Default to 10

        return user_selected_value
class MyTaskView(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = "tasks"
    template_name = "tasks/myTask.html"

    def get_queryset(self, **kwargs):
        qs = super().get_queryset(**kwargs)
        return qs.filter(assign_to_id=self.request.user.id)


class MyCreatedTaskView(LoginRequiredMixin, ListView):
    template_name = "tasks/myCreatedTask.html"
    model = Task
    context_object_name = "tasks"

    def get_queryset(self, **kwargs):
        qs = super().get_queryset(**kwargs)
        return qs.filter(creator_id=self.request.user.id)


class CreateTaskView(PermissionRequiredMixin, CreateView):
    template_name = "tasks/create_task.html"
    form_class = CreateTaskForm
    success_url = reverse_lazy("index:home")
    permission_required = "tasks.add_task"

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


class TaskDetailView(PermissionRequiredMixin, DetailView):
    model = Task
    template_name = "tasks/detail.html"
    permission_required = "tasks.view_task"


class TaskUpdate(PermissionRequiredMixin, UpdateView):
    model = Task
    fields = ("title", "description", "type", "status")
    template_name = "tasks/update.html"
    success_url = reverse_lazy("tasks:task_list")
    permission_required = "tasks.change_task"


class TaskDelete(PermissionRequiredMixin, DeleteView):
    model = Task
    template_name = "tasks/delete.html"
    success_url = reverse_lazy("tasks:task_list")
    permission_required = "tasks.delete_task"


class MyTeamTasks(ListView):
    model = Task
    template_name = "tasks/my_team_tasks.html"
    context_object_name = "tasks"

    def get_queryset(self, **kwargs):
        qs = super().get_queryset(**kwargs)
        return qs.filter(type__assigned_to=self.request.user.member_of)


class TaskDetailLogView(LoginRequiredMixin, ListView):
    model = TaskLog
    template_name = "tasks/change_log.html"
    context_object_name = "log"

    def get_queryset(self):
        task = get_object_or_404(Task, pk=self.kwargs["pk"])
        return task.log.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["task"] = get_object_or_404(Task, pk=self.kwargs["pk"])
        return context
