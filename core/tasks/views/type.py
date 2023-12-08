from django.views.generic import  DetailView
from ..models import TaskType
from django.urls import reverse_lazy
from ..forms import CreateTaskTypeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from ..filters import TypeFilter
from .task import Task
from base.views import BaseDeleteView, BaseListView, BaseCreateView,BaseUpdateView



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


class TypeCreateView(BaseCreateView):
    template_name = "tasks/type/create.html"
    form_class = CreateTaskTypeForm
    permission_required = 'tasks.add_tasktype'
    success_message = 'Task Type Successfully Created!'

    def get_success_url(self):
        return reverse_lazy("tasks:detail_type", kwargs={"pk": self.object.pk})


class TypeUpdateView(BaseUpdateView):
    model = TaskType
    fields = ("name", "description", "is_active")
    template_name = "tasks/type/update.html"
    permission_required = 'tasks.change_tasktype'
    success_message = 'Task Type successfully updated!'
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
