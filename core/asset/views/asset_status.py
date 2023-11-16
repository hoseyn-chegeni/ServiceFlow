from django.views.generic import (
    ListView,
    DeleteView,
    CreateView,
    UpdateView,
    DetailView,
)
from ..models.asset_status import AssetStatus
from django.urls import reverse_lazy
from ..forms import CreateAssetStatusForm


class AssetStatusListView(ListView):
    model = AssetStatus
    template_name = "asset/status/list.html"
    context_object_name = "asset"


class AssetStatusDetailView(DetailView):
    model = AssetStatus
    template_name = "asset/status/detail.html"


class AssetStatusCreateView(CreateView):
    model = AssetStatus
    template_name = "asset/status/create.html"
    form_class = CreateAssetStatusForm

    def get_success_url(self):
        return reverse_lazy("asset:status_list")

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class AssetStatusUpdateView(UpdateView):
    model = AssetStatus
    template_name = "asset/status/update.html"
    fields = (
        "name",
        "description",
    )

    success_url = reverse_lazy("asset:status_list")


class AssetStatusDeleteView(DeleteView):
    model = AssetStatus
    template_name = "asset/status/delete.html"
    success_url = reverse_lazy("asset:status_list")
