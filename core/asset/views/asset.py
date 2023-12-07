from django.views.generic import DeleteView, CreateView, UpdateView, DetailView
from django_filters.views import FilterView
from ..models.asset import Asset
from django.urls import reverse_lazy
from ..forms import CreateAssetForm
from ..filters import AssetFilters
from django.contrib.auth.mixins import LoginRequiredMixin


class AssetListView(LoginRequiredMixin, FilterView):
    model = Asset
    template_name = "asset/list.html"
    filterset_class = AssetFilters
    context_object_name = "asset"

    def get_paginate_by(self, queryset):
        # Get the value for paginate_by dynamically (e.g., from a form input or session)
        # Example: Set paginate_by to a user-selected value stored in session
        user_selected_value = self.request.session.get(
            "items_per_page", 10
        )  # Default to 10
        return user_selected_value



class AssetDetailView(LoginRequiredMixin, DetailView):
    model = Asset
    template_name = "asset/detail.html"


class AssetCreateView(LoginRequiredMixin, CreateView):
    model = Asset
    template_name = "asset/create.html"
    form_class = CreateAssetForm

    def get_success_url(self):
        return reverse_lazy("asset:list")

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class AssetUpdateView(LoginRequiredMixin, UpdateView):
    model = Asset
    template_name = "asset/update.html"
    fields = (
        "name",
        "type",
        "manufacturer",
        "model",
        "location",
        "assigned_user",
        "status",
        "maintenance_schedule",
        "purchase_cost",
        "depreciation_rate",
        "assigned_ip_address",
        "software_installed",
        "notes",
    )

    success_url = reverse_lazy("asset:list")


class AssetDeleteView(LoginRequiredMixin, DeleteView):
    model = Asset
    template_name = "asset/delete.html"
    success_url = reverse_lazy("asset:list")
