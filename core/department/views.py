from typing import Any
from django.shortcuts import render
from django.urls import reverse_lazy
from django_filters.views import FilterView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView

from .models import Department
from .filters import DepartmentFilters
from .forms import DepartmentCreateForm


# Create your views here.
class DepartmentListView(PermissionRequiredMixin, FilterView):
    model = Department
    filterset_class = DepartmentFilters
    context_object_name = "department"
    template_name = "department/list.html"
    permission_required = "department.view_department"


class DepartmentDetailView(PermissionRequiredMixin, DetailView):
    model = Department
    template_name = "department/detail.html"
    permission_required = "department.view_Department"

    # def get_context_data(self, **kwargs: Any):
    #     context = super().get_context_data(**kwargs)
        
    #     context["department"] = self.object.department.all()
    #     return context


class DepartmentCreateView(PermissionRequiredMixin, CreateView):
    model = Department
    template_name = "department/create.html"
    form_class = DepartmentCreateForm
    success_url = reverse_lazy("department:list")
    permission_required = "department.add_department"

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class DepartmentUpdateView(PermissionRequiredMixin, UpdateView):
    model = Department
    template_name = "department/update.html"
    fields = (
        "name",
        "description",
        "manager",
        "active_status",
        "organization",
    )
    success_url = reverse_lazy("department:list")
    permission_required = "department.change_department"


class DepartmentDeleteView(PermissionRequiredMixin, DeleteView):
    model = Department
    template_name = "department/delete.html"
    success_url = reverse_lazy("department:list")
    permission_required = "department.delete_department"
