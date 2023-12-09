from django.views.generic import DetailView
from ..models.asset_type import AssetType
from django.urls import reverse_lazy
from ..forms import CreateAssetTypeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from base.views import  BaseCreateView,BaseUpdateView,BaseDeleteView,BaseListView
from ..filters import AssetTypeFilters


class AssetTypeListView(BaseListView):
    model = AssetType
    template_name = "asset/type/list.html"
    context_object_name = "asset"
    filterset_class = AssetTypeFilters
    permission_required = 'asset.view_assettype'


class AssetTypeDetailView(LoginRequiredMixin, DetailView):
    model = AssetType
    template_name = "asset/type/detail.html"


class AssetTypeCreateView(BaseCreateView):
    model = AssetType
    template_name = "asset/type/create.html"
    form_class = CreateAssetTypeForm
    permission_required = 'asset.add_assettype'
    success_message = 'Type Successfully Created.'


    def get_success_url(self):
        return reverse_lazy("asset:type_detail", kwargs={"pk": self.object.pk})





class AssetTypeUpdateView(BaseUpdateView):
    model = AssetType
    template_name = "asset/type/update.html"
    permission_required = 'asset.change_assettype'
    success_message = 'Type Successfully Updated.'
    fields = (
        "name",
        "description",
    )

    def get_success_url(self):
        return reverse_lazy("asset:type_detail", kwargs={"pk": self.object.pk})


class AssetTypeDeleteView(BaseDeleteView):
    model = AssetType
    template_name = "asset/type/delete.html"
    success_url = reverse_lazy("asset:type_list")
    permission_required = 'asset.delete_assettype'
    message = 'Type Successfully Deleted'

