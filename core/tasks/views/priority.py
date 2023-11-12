from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
)
from ..models import TaskPriority
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
