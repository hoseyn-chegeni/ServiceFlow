from django.shortcuts import get_object_or_404
from ..filters import TaskFilter
from ..models import Task, TaskLogFlow, TaskStatus
from ..forms import CreateTaskForm, TaskLogFlowForm
from django.urls import reverse_lazy
from db_events.models import TaskLog
from db_events.filters import TaskLogFilter
from base.views import (
    BaseCreateView,
    BaseDeleteView,
    BaseListView,
    BaseUpdateView,
    BaseDetailView,
)
from django.views.generic import CreateView

class TaskView(BaseListView):
    model = Task
    filterset_class = TaskFilter
    context_object_name = "tasks"
    template_name = "tasks/tasks.html"
    permission_required = "tasks.view_task"


class MyTaskView(BaseListView):
    model = Task
    context_object_name = "tasks"
    template_name = "tasks/myTask.html"
    filterset_class = TaskFilter
    permission_required = "tasks.view_task"

    def get_queryset(self, **kwargs):
        qs = super().get_queryset(**kwargs)
        return qs.filter(assign_to_id=self.request.user.id)


class MyCreatedTaskView(BaseListView):
    template_name = "tasks/myCreatedTask.html"
    model = Task
    context_object_name = "tasks"
    filterset_class = TaskFilter
    permission_required = "tasks.view_task"

    def get_queryset(self, **kwargs):
        qs = super().get_queryset(**kwargs)
        return qs.filter(created_by_id=self.request.user.id)


class MyTeamTasks(BaseListView):
    model = Task
    template_name = "tasks/my_team_tasks.html"
    context_object_name = "tasks"
    filterset_class = TaskFilter
    permission_required = "tasks.view_task"

    def get_queryset(self, **kwargs):
        qs = super().get_queryset(**kwargs)
        return qs.filter(type__assigned_to=self.request.user.member_of)


class CreateTaskView(BaseCreateView):
    template_name = "tasks/create_task.html"
    form_class = CreateTaskForm
    permission_required = "tasks.add_task"
    success_message = "Task Successfully Created"
    url = "tasks:detail"

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        task = form.save(commit=False)
        task.team = task.type.work_flow.root.team
        task.status = TaskStatus.objects.get(name = 'Open')
        task.save()
        for i  in task.type.work_flow.root.action.all():
            task.actions.add(i)
        task.save()

        TaskLogFlow.objects.create(
            task = task, 
            flow = task.type.work_flow,
            state = task.type.work_flow.root,
            comment = f'Task Created with {task.type} type and send to {task.type.work_flow.root.team} for review'
        )
        return super().form_valid(form)

class TaskDetailView(BaseDetailView):
    model = Task
    template_name = "tasks/detail.html"
    permission_required = "tasks.view_task"


class TaskUpdate(BaseUpdateView):
    model = Task
    fields = ("title", "description", "type", "status")
    template_name = "tasks/update.html"
    permission_required = "tasks.change_task"
    success_message = "Task Successfully Updated"
    url = "tasks:detail"


    def form_valid(self, form):
        task = form.save(commit=False)
        task.participants.add(self.request.user)
        task.save()

        TaskLog.objects.create(
            task=task,
            user=self.request.user,
            event_type="Update Information",
            additional_info=f"{self.request.user} Updated Task Information at {task.last_change}",
        )
        return super().form_valid(form)
    

class TaskDelete(BaseDeleteView):
    model = Task
    template_name = "tasks/delete.html"
    success_url = reverse_lazy("tasks:task_list")
    permission_required = "tasks.delete_task"
    message = "Task Successfully Deleted!"


class TaskDetailLogView(BaseListView):
    model = TaskLog
    template_name = "tasks/change_log.html"
    context_object_name = "log"
    filterset_class = TaskLogFilter
    permission_required = "db_events.view_tasklog"

    def get_queryset(self):
        task = get_object_or_404(Task, pk=self.kwargs["pk"])
        return task.log.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["task"] = get_object_or_404(Task, pk=self.kwargs["pk"])
        return context


class TaskLogFlowCreateView(CreateView):
    model = TaskLogFlow
    form_class = TaskLogFlowForm
    template_name = 'tasks/c.html'

    def get_success_url(self):
        return reverse_lazy('tasks:detail', kwargs={"pk": self.task.pk})# Replace 'task_detail' with your task detail URL name
    
    def dispatch(self, request, *args, **kwargs):
        self.task = get_object_or_404(Task, pk=self.kwargs['pk'])
        return super().dispatch(request, *args, **kwargs)
    
    def get_form_kwargs(self):
        kwargs = super(TaskLogFlowCreateView, self).get_form_kwargs()
        kwargs['initial']['task'] = self.task
        return kwargs
    


    def form_valid(self, form):
        action = form.save(commit=False)
        form.instance.created_by = self.request.user
        form.instance.flow = self.task.type.work_flow
        form.instance.state = form.instance.action.next_state
        action.save()
        task = Task.objects.get(id = self.task.id)
        task.team  = form.instance.action.next_state.team
        task.save()
        return super().form_valid(form)
