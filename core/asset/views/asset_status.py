from django.views.generic import ListView, DetailView
from ..models.asset_status import AssetStatus
from ..models.asset import Asset
from django.urls import reverse_lazy
from ..forms import CreateAssetStatusForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count
from base.views import BaseCreateView, BaseDeleteView, BaseListView, BaseUpdateView, BaseDetailView
from ..filters import AssetStatusFilters


class AssetStatusListView(BaseListView):
    model = AssetStatus
    template_name = "asset/status/list.html"
    context_object_name = "status_counts"
    filterset_class = AssetStatusFilters
    queryset = AssetStatus.objects.annotate(asset_count=Count("asset"))
    permission_required = "asset.view_assetstatus"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["status_counts"] = self.queryset.values_list(
            "id",
            "name",
            "asset_count",
            "is_active",
        )
        context["BYOD"] = Asset.objects.filter(byod=True).count()
        return context


class AssetStatusDetailView(BaseDetailView):
    model = AssetStatus
    template_name = "asset/status/detail.html"
    permission_required = "asset.change_assetstatus"

class AssetStatusCreateView(BaseCreateView):
    model = AssetStatus
    template_name = "asset/status/create.html"
    form_class = CreateAssetStatusForm
    permission_required = "asset.add_assetstatus"
    success_message = "Status Successfully Added."
    url = "asset:status_detail"


class AssetStatusUpdateView(BaseUpdateView):
    model = AssetStatus
    template_name = "asset/status/update.html"
    permission_required = "asset.change_assetstatus"
    success_message = "Status Successfully Updated."
    context_object_name = 'asset_status'
    fields = (
        "name",
        "description",
    )
    url = "asset:status_detail"


class AssetStatusDeleteView(BaseDeleteView):
    model = AssetStatus
    template_name = "asset/status/delete.html"
    success_url = reverse_lazy("asset:status_list")
    message = "Status Successfully Deleted."
    permission_required = "asset.delete_assetstatus"


class AllBYODListView(LoginRequiredMixin, ListView):
    model = Asset
    template_name = "asset/status/BYOD.html"
    context_object_name = "byod"

    def get_queryset(self, **kwargs):
        qs = super().get_queryset(**kwargs)
        return qs.filter(byod=True)
