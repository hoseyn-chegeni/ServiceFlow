from django.shortcuts import get_object_or_404, HttpResponseRedirect
from django.views.generic import (
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
)
from ..models import TaskPriority, Task
from django.urls import reverse_lazy
from ..forms import CreateTaskPriorityForm
from db_events.models import TaskLog
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django_filters.views import FilterView
from ..filters import PriorityFilter
from django.contrib.messages.views import SuccessMessageMixin


class PriorityListView(LoginRequiredMixin, FilterView):
    model = TaskPriority
    context_object_name = "priorities"
    template_name = "tasks/priority/list.html"
    filterset_class = PriorityFilter
    success_message = "New Priority Successfully Added"

    def get_paginate_by(self, queryset):
        # Get the value for paginate_by dynamically (e.g., from a form input or session)
        # Example: Set paginate_by to a user-selected value stored in session
        user_selected_value = self.request.session.get(
            "items_per_page", 10
        )  # Default to 10
        return user_selected_value


class PriorityDetailView(LoginRequiredMixin, DetailView):
    model = TaskPriority
    template_name = "tasks/priority/detail.html"
    context_object_name = "priority"


class PriorityCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = "tasks/priority/create.html"
    form_class = CreateTaskPriorityForm
    success_message = "Priority successfully Created."

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("tasks:detail_priority", kwargs={"pk": self.object.pk})

    def get_success_message(self, cleaned_data):
        return self.success_message


class PriorityUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = TaskPriority
    fields = (
        "name",
        "description",
        "is_active",
        "badge",
    )
    template_name = "tasks/priority/update.html"
    success_message = "Priority Successfully Updated"

    def get_success_url(self):
        return reverse_lazy("tasks:detail_priority", kwargs={"pk": self.object.pk})

    def get_success_message(self, cleaned_data):
        return self.success_message


class PriorityDeleteView(LoginRequiredMixin, DeleteView):
    model = TaskPriority
    template_name = "tasks/priority/delete.html"
    success_url = reverse_lazy("tasks:list_priority")

    def get(self, request, *args, **kwargs):
        # Get the object to be deleted
        self.object = self.get_object()

        # Perform the delete operation directly without displaying a confirmation template
        success_url = self.get_success_url()
        self.object.delete()
        messages.success(self.request, f"Task successfully Deleted!")
        return HttpResponseRedirect(success_url)


class ChangePriorityView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = "tasks/priority/change.html"
    model = Task
    fields = ("priority",)
    success_message = "Task Priority successfully Changed"

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

    def get_success_message(self, cleaned_data):
        return self.success_message


class TaskWithThisPriority(LoginRequiredMixin, DetailView):
    model = TaskPriority
    template_name = "tasks/priority/task_priority.html"
    context_object_name = "priority"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["task"] = Task.objects.filter(priority_id=self.object.pk)

        return context
