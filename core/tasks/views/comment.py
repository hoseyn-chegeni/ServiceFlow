from django.shortcuts import get_object_or_404
from django.views.generic import (
    CreateView,
)

from ..models import Task, TaskComment
from django.urls import reverse_lazy
from db_events.models import TaskLog
from base.views import BaseCreateView

class TaskCommentView(BaseCreateView):
    model = TaskComment
    template_name = "tasks/task_comment.html"
    fields = ["comment", "attachments", "attachment_title"]
    success_message = "New Comment Successfully Added to Task."
    permission_required = 'tasks.add_taskcomment'
    def form_valid(self, form):
        task = get_object_or_404(Task, pk=self.kwargs["pk"])
        task.participants.add(self.request.user)
        form.instance.task = task
        form.instance.user = self.request.user

        TaskLog.objects.create(
            task=task,
            user=self.request.user,
            event_type="Add Comment",
            additional_info=f"{self.request.user} Added A Comment '{form.instance.comment}' for {task}",
        )
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("tasks:detail", args=[self.kwargs["pk"]])

    def get_initial(self):
        initial = super().get_initial()
        initial["attachment_title"] = self.model._meta.get_field(
            "attachment_title"
        ).get_default()
        return initial
