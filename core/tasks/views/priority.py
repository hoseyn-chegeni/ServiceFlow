from django.shortcuts import get_object_or_404
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
)
from ..models import TaskPriority, Task
from django.urls import reverse_lazy
from ..forms import CreateTaskPriorityForm
from db_events.models import TaskLog
from django.contrib.auth.mixins import LoginRequiredMixin

class PriorityListView(LoginRequiredMixin, ListView):
    model = TaskPriority
    context_object_name = "priority"
    template_name = "tasks/priority/list.html"


class PriorityDetailView(LoginRequiredMixin, DetailView):
    model = TaskPriority
    template_name = "tasks/priority/detail.html"
    context_object_name = "priority"


class PriorityCreateView(LoginRequiredMixin, CreateView):
    template_name = "tasks/priority/create.html"
    form_class = CreateTaskPriorityForm

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("tasks:detail_priority", kwargs={"pk": self.object.pk})


class PriorityUpdateView(LoginRequiredMixin, UpdateView):
    model = TaskPriority
    fields = ("name", "description", "is_active")
    template_name = "tasks/priority/update.html"

    def get_success_url(self):
        return reverse_lazy("tasks:detail_priority", kwargs={"pk": self.object.pk})


class PriorityDeleteView(LoginRequiredMixin, DeleteView):
    model = TaskPriority
    template_name = "tasks/priority/delete.html"
    success_url = reverse_lazy("tasks:list_priority")


class ChangePriorityView(LoginRequiredMixin, UpdateView):
    template_name = "tasks/priority/change.html"
    model = Task
    fields = ("priority",)

    def form_valid(self, form):
        task = form.save(commit=False)
        task.save()

        TaskLog.objects.create(
            task=task,
            user=self.request.user,
            event_type="Priority Change",
            additional_info=f"{self.request.user} Set '{task.priority}' Priority for {task}",
        )
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("tasks:detail", kwargs={"pk": self.object.pk})
