from typing import Any
from django.shortcuts import render
from django.urls import reverse_lazy
from django_filters.views import FilterView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView

from .models import Organization
from .filters import OrganizationFilters
from .forms import OrganizationCreateForm


# Create your views here.
class OrganizationListView(PermissionRequiredMixin, FilterView):
    model = Organization
    filterset_class = OrganizationFilters
    context_object_name = "orgs"
    template_name = "organization/list.html"
    permission_required = "organization.view_organization"


class OrganizationDetailView(PermissionRequiredMixin, DetailView):
    model = Organization
    template_name = "organization/detail.html"
    permission_required = "organization.view_organization"


class OrganizationCreateView(PermissionRequiredMixin, CreateView):
    model = Organization
    template_name = "organization/create.html"
    form_class = OrganizationCreateForm
    success_url = reverse_lazy("organization:list")
    permission_required = "organization.add_organization"

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class OrganizationUpdateView(PermissionRequiredMixin, UpdateView):
    model = Organization
    template_name = "organization/update.html"
    fields = (
        "name",
        "address",
        "postal_code",
        "phone_number",
        "email",
        "industry",
        "employee_count",
        "founding_date",
        "parent_organization",
        "subsidiaries",
        "legal_entity_type",
        "tax_id_number",
        "registration_number",
        "registration_date",
        "logo",
    )
    success_url = reverse_lazy("organization:list")
    permission_required = "organization.change_organization"


class OrganizationDeleteView(PermissionRequiredMixin, DeleteView):
    model = Organization
    template_name = "organization/delete.html"
    success_url = reverse_lazy("organization:list")
    permission_required = "organization.delete_organization"
