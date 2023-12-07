from django.shortcuts import get_object_or_404, HttpResponseRedirect
from django_filters.views import FilterView
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
)
from ..filters import TaskFilter
from ..models import Task
from ..forms import CreateTaskForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from db_events.models import TaskLog
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from db_events.filters import TaskLogFilter


class TaskView(LoginRequiredMixin, FilterView):
    model = Task
    filterset_class = TaskFilter
    context_object_name = "tasks"
    template_name = "tasks/tasks.html"

    def get_paginate_by(self, queryset):
        # Get the value for paginate_by dynamically (e.g., from a form input or session)
        # Example: Set paginate_by to a user-selected value stored in session
        user_selected_value = self.request.session.get(
            "items_per_page", 10
        )  # Default to 10

        return user_selected_value
    
class MyTaskView(LoginRequiredMixin, FilterView):
    model = Task
    context_object_name = "tasks"
    template_name = "tasks/myTask.html"
    filterset_class = TaskFilter

    def get_queryset(self, **kwargs):
        qs = super().get_queryset(**kwargs)
        return qs.filter(assign_to_id=self.request.user.id)

    def get_paginate_by(self, queryset):
        # Get the value for paginate_by dynamically (e.g., from a form input or session)
        # Example: Set paginate_by to a user-selected value stored in session
        user_selected_value = self.request.session.get(
            "items_per_page", 10
        )  # Default to 10

class MyCreatedTaskView(LoginRequiredMixin, FilterView):
    template_name = "tasks/myCreatedTask.html"
    model = Task
    context_object_name = "tasks"
    filterset_class = TaskFilter

    def get_queryset(self, **kwargs):
        qs = super().get_queryset(**kwargs)
        return qs.filter(creator_id=self.request.user.id)

    def get_paginate_by(self, queryset):
        # Get the value for paginate_by dynamically (e.g., from a form input or session)
        # Example: Set paginate_by to a user-selected value stored in session
        user_selected_value = self.request.session.get(
            "items_per_page", 10
        )  # Default to 10


class MyTeamTasks(LoginRequiredMixin, FilterView):
    model = Task
    template_name = "tasks/my_team_tasks.html"
    context_object_name = "tasks"
    filterset_class = TaskFilter

    def get_queryset(self, **kwargs):
        qs = super().get_queryset(**kwargs)
        return qs.filter(type__assigned_to=self.request.user.member_of)
    
    def get_paginate_by(self, queryset):
        # Get the value for paginate_by dynamically (e.g., from a form input or session)
        # Example: Set paginate_by to a user-selected value stored in session
        user_selected_value = self.request.session.get(
            "items_per_page", 10
        )  # Default to 10

        
class CreateTaskView(PermissionRequiredMixin,SuccessMessageMixin,  CreateView):
    template_name = "tasks/create_task.html"
    form_class = CreateTaskForm
    permission_required = "tasks.add_task"
    success_message = 'Task Successfully Created'
    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('tasks:detail', kwargs={'pk': self.object.pk})  
    
    def get_success_message(self, cleaned_data):
        return self.success_message


class TaskDetailView(PermissionRequiredMixin, DetailView):
    model = Task
    template_name = "tasks/detail.html"
    permission_required = "tasks.view_task"


class TaskUpdate(PermissionRequiredMixin,SuccessMessageMixin, UpdateView):
    model = Task
    fields = ("title", "description", "type", "status")
    template_name = "tasks/update.html"
    permission_required = "tasks.change_task"
    success_message = 'Task Successfully Updated'

    def get_success_url(self):
        return reverse_lazy('tasks:detail', kwargs={"pk": self.object.pk})

    def get_success_message(self, cleaned_data):
        return self.success_message

class TaskDelete(PermissionRequiredMixin, DeleteView):
    model = Task
    template_name = "tasks/delete.html"
    success_url = reverse_lazy("tasks:task_list")
    permission_required = "tasks.delete_task"

    def get(self, request, *args, **kwargs):
        # Get the object to be deleted
        self.object = self.get_object()

        # Perform the delete operation directly without displaying a confirmation template
        success_url = self.get_success_url()
        self.object.delete()
        messages.success(
                self.request, f"Task successfully Deleted!"
            )
        return HttpResponseRedirect(success_url)



class TaskDetailLogView(LoginRequiredMixin, FilterView):
    model = TaskLog
    template_name = "tasks/change_log.html"
    context_object_name = "log"
    filterset_class = TaskLogFilter

    def get_queryset(self):
        task = get_object_or_404(Task, pk=self.kwargs["pk"])
        return task.log.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["task"] = get_object_or_404(Task, pk=self.kwargs["pk"])
        return context
    

    def get_paginate_by(self, queryset):
        # Get the value for paginate_by dynamically (e.g., from a form input or session)
        # Example: Set paginate_by to a user-selected value stored in session
        user_selected_value = self.request.session.get(
            "items_per_page", 10
        )  # Default to 10
        return user_selected_value
