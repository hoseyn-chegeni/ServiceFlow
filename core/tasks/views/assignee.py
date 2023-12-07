from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, HttpResponseRedirect
from django.views import View
from django.contrib import messages 
from django.views.generic import (
    ListView,
    UpdateView,
)
from ..models import Task
from db_events.models import TaskLog
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin


class TaskAssignToMe(LoginRequiredMixin,View):
    def get(self, request, pk):
        task = Task.objects.filter(pk=pk).first()
        if task:
            task.assign_to = self.request.user
            task.participants.add(self.request.user)
            messages.success(
                self.request, f"TSK-{task.id} Successfully assigned to you."
            )
            task.save()
            TaskLog.objects.create(
            user=self.request.user,
            task=task,
            event_type="Assignment",
            additional_info=f"{self.request.user} Assigned Task to {task.assign_to}",
        )
        return HttpResponseRedirect(reverse_lazy("tasks:detail", kwargs={'pk': task.pk}))



class TaskAssignTo(LoginRequiredMixin,SuccessMessageMixin, UpdateView):
    template_name = "tasks/assign_to.html"
    model = Task
    fields = ("assign_to",)
    success_message = "Task successfully assigned."

    def form_valid(self, form):
        task = form.save(commit=False)
        task.save()
        task.participants.add(task.assign_to)
        task.participants.add(self.request.user)
        task.save()

        TaskLog.objects.create(
            user=self.request.user,
            task=task,
            event_type="Assignment",
            additional_info=f"{self.request.user} Assigned Task to {task.assign_to}",
        )
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('tasks:detail',kwargs={"pk": self.object.pk})
    
    def get_success_message(self, cleaned_data):
        return self.success_message