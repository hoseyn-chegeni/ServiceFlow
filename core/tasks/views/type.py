from django.views.generic import (
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
)
from ..models import TaskType
from django.urls import reverse_lazy
from ..forms import CreateTaskTypeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import HttpResponseRedirect
from django_filters.views import FilterView
from ..filters import TypeFilter
from .task import Task
from base.views import BaseDeleteView, BaseListView

class TypeListView(BaseListView):
    model = TaskType
    context_object_name = "type"
    template_name = "tasks/type/list.html"
    filterset_class = TypeFilter
    permission_required = 'tasks.view_tasktype'




class TypeDetailView(LoginRequiredMixin, DetailView):
    model = TaskType
    template_name = "tasks/type/detail.html"
    context_object_name = "type"


class TypeCreateView(LoginRequiredMixin, CreateView):
    template_name = "tasks/type/create.html"
    form_class = CreateTaskTypeForm

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("tasks:detail_type", kwargs={"pk": self.object.pk})


class TypeUpdateView(LoginRequiredMixin, UpdateView):
    model = TaskType
    fields = ("name", "description", "is_active")
    template_name = "tasks/type/update.html"

    def get_success_url(self):
        return reverse_lazy("tasks:detail_type", kwargs={"pk": self.object.pk})


class TypeDeleteView(BaseDeleteView):
    model = TaskType
    template_name = "tasks/type/delete.html"
    success_url = reverse_lazy("tasks:list_type")
    message = 'Task successfully Deleted!'
    permission_required = 'task.delete_tasktype'


class TaskWithThisType(LoginRequiredMixin, DetailView):
    model = TaskType
    template_name = "tasks/type/task_type.html"
    context_object_name = "type"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["task"] = Task.objects.filter(type_id=self.object.pk)
        return context
