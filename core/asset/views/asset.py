from django.views.generic import DetailView
from ..models.asset import Asset
from django.urls import reverse_lazy
from ..forms import CreateAssetForm
from ..filters import AssetFilters
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from base.views import BaseDeleteView, BaseListView, BaseCreateView,BaseUpdateView


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



class AssetCreateView(BaseCreateView):
    model = Asset
    template_name = "asset/create.html"
    form_class = CreateAssetForm
    permission_required = "asset.add_asset"
    success_message = 'Asset Successfully Added'

    def get_success_url(self):
        return reverse_lazy("asset:detail", kwargs={"pk": self.object.pk})



class AssetUpdateView(BaseUpdateView):
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

    def get_success_url(self):
        return reverse_lazy("asset:detail", kwargs={"pk": self.object.pk})


class AssetDeleteView(BaseDeleteView):
    model = Asset
    template_name = "asset/delete.html"
    success_url = reverse_lazy("asset:list")
    permission_required = "asset.delete_asset"
    message = "Asset Successfully Deleted!"
