from django.shortcuts import get_object_or_404, HttpResponseRedirect
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
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from db_events.filters import TaskLogFilter
from base.views import BaseCreateView, BaseDeleteView, BaseListView, BaseUpdateView


class TaskView(BaseListView):
    model = Task
    filterset_class = TaskFilter
    context_object_name = "tasks"
    template_name = "tasks/tasks.html"
    permission_required = "tasks.view_task"


class MyTaskView(BaseListView):
    model = Task
    context_object_name = "tasks"
    template_name = "tasks/myTask.html"
    filterset_class = TaskFilter
    permission_required = "tasks.view_task"

    def get_queryset(self, **kwargs):
        qs = super().get_queryset(**kwargs)
        return qs.filter(assign_to_id=self.request.user.id)


class MyCreatedTaskView(BaseListView):
    template_name = "tasks/myCreatedTask.html"
    model = Task
    context_object_name = "tasks"
    filterset_class = TaskFilter
    permission_required = "tasks.view_task"

    def get_queryset(self, **kwargs):
        qs = super().get_queryset(**kwargs)
        return qs.filter(creator_id=self.request.user.id)


class MyTeamTasks(BaseListView):
    model = Task
    template_name = "tasks/my_team_tasks.html"
    context_object_name = "tasks"
    filterset_class = TaskFilter
    permission_required = "tasks.view_task"

    def get_queryset(self, **kwargs):
        qs = super().get_queryset(**kwargs)
        return qs.filter(type__assigned_to=self.request.user.member_of)


class CreateTaskView(BaseCreateView):
    template_name = "tasks/create_task.html"
    form_class = CreateTaskForm
    permission_required = "tasks.add_task"
    success_message = "Task Successfully Created"

    def get_success_url(self):
        return reverse_lazy("tasks:detail", kwargs={"pk": self.object.pk})


class TaskDetailView(PermissionRequiredMixin, DetailView):
    model = Task
    template_name = "tasks/detail.html"
    permission_required = "tasks.view_task"


class TaskUpdate(BaseUpdateView):
    model = Task
    fields = ("title", "description", "type", "status")
    template_name = "tasks/update.html"
    permission_required = "tasks.change_task"
    success_message = "Task Successfully Updated"

    def get_success_url(self):
        return reverse_lazy("tasks:detail", kwargs={"pk": self.object.pk})


class TaskDelete(BaseDeleteView):
    model = Task
    template_name = "tasks/delete.html"
    success_url = reverse_lazy("tasks:task_list")
    permission_required = "tasks.delete_task"
    message = "Task Successfully Deleted!"


class TaskDetailLogView(BaseListView):
    model = TaskLog
    template_name = "tasks/change_log.html"
    context_object_name = "log"
    filterset_class = TaskLogFilter
    permission_required = "db_events.view_tasklog"

    def get_queryset(self):
        task = get_object_or_404(Task, pk=self.kwargs["pk"])
        return task.log.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["task"] = get_object_or_404(Task, pk=self.kwargs["pk"])
        return context
