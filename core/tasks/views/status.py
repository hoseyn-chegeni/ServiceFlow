from django.shortcuts import get_object_or_404
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
)
from ..models import TaskStatus, Task
from django.urls import reverse_lazy
from ..forms import CreateTaskStatusForm
from db_events.models import TaskLog


class StatusListView(ListView):
    model = TaskStatus
    context_object_name = "status"
    template_name = "tasks/status/list.html"


class StatusDetailView(DetailView):
    model = TaskStatus
    template_name = "tasks/status/detail.html"
    context_object_name = "status"


class StatusCreateView(CreateView):
    template_name = "tasks/status/create.html"
    form_class = CreateTaskStatusForm

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("tasks:detail_status", kwargs={"pk": self.object.pk})


class StatusUpdateView(UpdateView):
    model = TaskStatus
    fields = ("name", "description", "is_active")
    template_name = "tasks/status/update.html"

    def get_success_url(self):
        return reverse_lazy("tasks:detail_status", kwargs={"pk": self.object.pk})


class StatusDeleteView(DeleteView):
    model = TaskStatus
    template_name = "tasks/status/delete.html"
    success_url = reverse_lazy("tasks:list_status")


class ChangeStatusView(UpdateView):
    template_name = "tasks/status/change_status.html"
    model = Task
    fields = ("status",)

    def form_valid(self, form):
        task = form.save(commit=False)
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
