from django.views.generic import (
    ListView,
    DeleteView,
    CreateView,
    UpdateView,
    DetailView,
)
from ..models.asset_type import AssetType
from django.urls import reverse_lazy
from ..forms import CreateAssetTypeForm


class AssetTypeListView(ListView):
    model = AssetType
    template_name = "asset/type/list.html"
    context_object_name = "asset"


class AssetTypeDetailView(DetailView):
    model = AssetType
    template_name = "asset/type/detail.html"


class AssetTypeCreateView(CreateView):
    model = AssetType
    template_name = "asset/type/create.html"
    form_class = CreateAssetTypeForm

    def get_success_url(self):
        return reverse_lazy("asset:type_list")

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class AssetTypeUpdateView(UpdateView):
    model = AssetType
    template_name = "asset/type/update.html"
    fields = (
        "name",
        "description",
    )

    success_url = reverse_lazy("asset:type_list")


class AssetTypeDeleteView(DeleteView):
    model = AssetType
    template_name = "asset/type/delete.html"
    success_url = reverse_lazy("asset:type_list")
