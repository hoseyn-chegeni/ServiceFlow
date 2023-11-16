from typing import Any
from django.shortcuts import get_object_or_404
from django.views.generic import (
    CreateView,
)

from ..models import Task, TaskComment
from django.urls import reverse_lazy


class TaskCommentView(CreateView):
    model = TaskComment
    template_name = "tasks/task_comment.html"
    fields = ["comment","attachments"]

    def form_valid(self, form):
        task = get_object_or_404(Task, pk=self.kwargs["pk"])
        form.instance.task = task
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("tasks:detail", args=[self.kwargs["pk"]])
