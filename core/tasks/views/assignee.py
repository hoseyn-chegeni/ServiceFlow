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


# class (LoginRequiredMixin, UpdateView):
#     template_name = "tasks/assign_to_me.html"
#     success_url = reverse_lazy("tasks:my_team")
#     model = Task
#     fields = ("assign_to",)

#     def form_valid(self, form):
#         task = form.save(commit=False)
#         task.save()
#         form.instance.assign_to = self.request.user


#         return super().form_valid(form)
    

class TaskAssignToMe(LoginRequiredMixin,View):
    def get(self, request, pk):
        task = Task.objects.filter(pk=pk).first()
        if task:
            task.assign_to = self.request.user
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



class TaskAssignTo(LoginRequiredMixin, UpdateView):
    template_name = "tasks/assign_to.html"
    success_url = reverse_lazy("tasks:my_team")
    model = Task
    fields = ("assign_to",)

    def form_valid(self, form):
        task = form.save(commit=False)
        task.save()

        TaskLog.objects.create(
            user=self.request.user,
            task=task,
            event_type="Assignment",
            additional_info=f"{self.request.user} Assigned Task to {task.assign_to}",
        )
        return super().form_valid(form)
