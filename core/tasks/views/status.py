from typing import Any
from django.views.generic import DetailView
from ..models import TaskStatus, Task
from django.urls import reverse_lazy
from ..forms import CreateTaskStatusForm
from db_events.models import TaskLog
from django.contrib.auth.mixins import LoginRequiredMixin
from ..filters import StatusFilter
from base.views import BaseListView,BaseCreateView,BaseDeleteView,BaseUpdateView

class StatusListView(BaseListView):
    model = TaskStatus
    context_object_name = "status"
    template_name = "tasks/status/list.html"
    filterset_class = StatusFilter
    permission_required = 'tasks.view_taskstatus'


class StatusDetailView(LoginRequiredMixin, DetailView):
    model = TaskStatus
    template_name = "tasks/status/detail.html"
    context_object_name = "status"


class StatusCreateView(BaseCreateView):
    template_name = "tasks/status/create.html"
    form_class = CreateTaskStatusForm
    success_message = "Status Successfully Created"
    permission_required = 'tasks.add_taskstatus'

    def get_success_url(self):
        return reverse_lazy("tasks:detail_status", kwargs={"pk": self.object.pk})


class StatusUpdateView(BaseUpdateView):
    model = TaskStatus
    fields = ("name", "description", "is_active")
    template_name = "tasks/status/update.html"
    success_message = "Status Successfully Updated"
    permission_required  = 'tasks.change_taskstatus'

    def get_success_url(self):
        return reverse_lazy("tasks:detail_status", kwargs={"pk": self.object.pk})



class StatusDeleteView(BaseDeleteView):
    model = TaskStatus
    template_name = "tasks/status/delete.html"
    success_url = reverse_lazy("tasks:list_status")
    message = 'Status Successfully Deleted!'
    permission_required  = 'tasks.delete_taskstatus'

class ChangeStatusView(BaseUpdateView):
    template_name = "tasks/status/change_status.html"
    model = Task
    fields = ("status",)
    success_message = "Task Status Successfully Changed."
    permission_required  = 'tasks.change_taskstatus'

    def form_valid(self, form):
        task = form.save(commit=False)
        task.participants.add(self.request.user)
        task.save()

        TaskLog.objects.create(
            task=task,
            user=self.request.user,
            event_type="Status Change",
            additional_info=f"{self.request.user} Set '{task.status}' Status for {task}",
        )

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("tasks:detail", kwargs={"pk": self.object.pk})



class TaskWithThisStatus(LoginRequiredMixin, DetailView):
    model = TaskStatus
    template_name = "tasks/status/task_status.html"
    context_object_name = "status"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["task"] = Task.objects.filter(status_id=self.object.pk)

        return context
