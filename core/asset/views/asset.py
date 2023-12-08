from django.views.generic import CreateView, UpdateView, DetailView
from ..models.asset import Asset
from django.urls import reverse_lazy
from ..forms import CreateAssetForm
from ..filters import AssetFilters
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from base.views import BaseDeleteView, BaseListView


class AssetListView(BaseListView):
    model = Asset
    template_name = "asset/list.html"
    filterset_class = AssetFilters
    context_object_name = "asset"
    permission_required = "asset.view_asset"


class AssetDetailView(PermissionRequiredMixin, LoginRequiredMixin, DetailView):
    model = Asset
    template_name = "asset/detail.html"
    permission_required = "asset.view_asset"


class AssetCreateView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    model = Asset
    template_name = "asset/create.html"
    form_class = CreateAssetForm
    permission_required = "asset.add_asset"

    def get_success_url(self):
        return reverse_lazy("asset:list")

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class AssetUpdateView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Asset
    template_name = "asset/update.html"
    context_object_name = "asset"
    permission_required = "asset.change_asset"

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


class AssetDeleteView(BaseDeleteView):
    model = Asset
    template_name = "asset/delete.html"
    success_url = reverse_lazy("asset:list")
    permission_required = "asset.delete_asset"
    message = "Asset Successfully Deleted!"
