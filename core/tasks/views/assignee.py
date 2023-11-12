from typing import Any
from django.shortcuts import get_object_or_404
from django.views.generic import (
    ListView,
    UpdateView,
)
from ..models import Task, TaskAssignmentHistory
from django.urls import reverse_lazy


class TaskAssignToMe(UpdateView):
    template_name = "tasks/assign_to_me.html"
    success_url = reverse_lazy("tasks:my_team")
    model = Task
    fields = ("assign_to",)

    def form_valid(self, form):
        task = form.save(commit=False)
        task.save()
        form.instance.assign_to = self.request.user
        TaskAssignmentHistory.objects.create(
            task=task, assigned_by=self.request.user, assigned_to=self.request.user
        )
        return super().form_valid(form)


class TaskAssignTo(UpdateView):
    template_name = "tasks/assign_to.html"
    success_url = reverse_lazy("tasks:my_team")
    model = Task
    fields = ("assign_to",)

    def form_valid(self, form):
        task = form.save(commit=False)
        task.save()

        TaskAssignmentHistory.objects.create(
            task=task, assigned_by=self.request.user, assigned_to=task.assign_to
        )
        return super().form_valid(form)


class TaskAssignmentLogsView(ListView):
    model = TaskAssignmentHistory
    template_name = "tasks/assign_log.html"
    context_object_name = "log"

    def get_queryset(self):
        task = get_object_or_404(Task, pk=self.kwargs["pk"])
        return task.assignment_history.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["task"] = get_object_or_404(Task, pk=self.kwargs["pk"])
        return context
