from django.shortcuts import get_object_or_404
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
)
from ..models import TaskPriority, Task, TaskPriorityChange
from django.urls import reverse_lazy
from ..forms import CreateTaskPriorityForm


class PriorityListView(ListView):
    model = TaskPriority
    context_object_name = "priority"
    template_name = "tasks/priority/list.html"


class PriorityDetailView(DetailView):
    model = TaskPriority
    template_name = "tasks/priority/detail.html"
    context_object_name = "priority"


class PriorityCreateView(CreateView):
    template_name = "tasks/priority/create.html"
    form_class = CreateTaskPriorityForm

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("tasks:detail_priority", kwargs={"pk": self.object.pk})


class PriorityUpdateView(UpdateView):
    model = TaskPriority
    fields = ("name", "description", "is_active")
    template_name = "tasks/priority/update.html"

    def get_success_url(self):
        return reverse_lazy("tasks:detail_priority", kwargs={"pk": self.object.pk})


class PriorityDeleteView(DeleteView):
    model = TaskPriority
    template_name = "tasks/priority/delete.html"
    success_url = reverse_lazy("tasks:list_priority")


class ChangePriorityView(UpdateView):
    template_name = "tasks/priority/change.html"
    model = Task
    fields = ("priority",)

    def form_valid(self, form):
        task = form.save(commit=False)
        task.save()

        TaskPriorityChange.objects.create(
            task=task, priority=task.priority, changed_by=self.request.user
        )
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("tasks:detail", kwargs={"pk": self.object.pk})


class ChangePriorityLogView(ListView):
    model = TaskPriorityChange
    template_name = "tasks/priority/log.html"
    context_object_name = "log"

    def get_queryset(self):
        task = get_object_or_404(Task, pk=self.kwargs["pk"])
        return task.priority_log.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["task"] = get_object_or_404(Task, pk=self.kwargs["pk"])
        return context
