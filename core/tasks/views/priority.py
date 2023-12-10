from ..models import TaskPriority, Task
from django.urls import reverse_lazy
from ..forms import CreateTaskPriorityForm
from db_events.models import TaskLog
from ..filters import PriorityFilter
from base.views import (
    BaseCreateView,
    BaseDeleteView,
    BaseListView,
    BaseUpdateView,
    BaseDetailView,
)


class PriorityListView(BaseListView):
    model = TaskPriority
    context_object_name = "priorities"
    template_name = "tasks/priority/list.html"
    filterset_class = PriorityFilter
    success_message = "New Priority Successfully Added"
    permission_required = "tasks.view_taskpriority"


class PriorityDetailView(BaseDetailView):
    model = TaskPriority
    template_name = "tasks/priority/detail.html"
    context_object_name = "priority"
    permission_required = "tasks.view_taskpriority"


class PriorityCreateView(BaseCreateView):
    template_name = "tasks/priority/create.html"
    form_class = CreateTaskPriorityForm
    success_message = "Priority successfully Created."
    permission_required = "tasks.add_taskpriority"
    url = "tasks:detail_priority"


class PriorityUpdateView(BaseUpdateView):
    model = TaskPriority
    url = "tasks:detail_priority"
    fields = (
        "name",
        "description",
        "is_active",
        "badge",
    )
    template_name = "tasks/priority/update.html"
    success_message = "Priority Successfully Updated"
    permission_required = "tasks.change_taskpriority"


class PriorityDeleteView(BaseDeleteView):
    model = TaskPriority
    template_name = "tasks/priority/delete.html"
    success_url = reverse_lazy("tasks:list_priority")
    permission_required = "tasks.delete_taskpriority"
    message = "Priority Successfully deleted"


class ChangePriorityView(BaseUpdateView):
    template_name = "tasks/priority/change.html"
    model = Task
    fields = ("priority",)
    success_message = "Task Priority successfully Changed"
    permission_required = "tasks.change_taskpriority"

    def form_valid(self, form):
        task = form.save(commit=False)
        task.participants.add(self.request.user)
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


class TaskWithThisPriority(BaseDetailView):
    model = TaskPriority
    template_name = "tasks/priority/task_priority.html"
    context_object_name = "priority"
    permission_required = "tasks.view_taskpriority"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["task"] = Task.objects.filter(priority_id=self.object.pk)
        return context
