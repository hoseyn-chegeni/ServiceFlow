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
from django.contrib.auth.mixins import LoginRequiredMixin


class AssetStatusListView(LoginRequiredMixin, ListView):
    model = AssetStatus
    template_name = "asset/status/list.html"
    context_object_name = "asset"


class AssetStatusDetailView(LoginRequiredMixin, DetailView):
    model = AssetStatus
    template_name = "asset/status/detail.html"


class AssetStatusCreateView(LoginRequiredMixin, CreateView):
    model = AssetStatus
    template_name = "asset/status/create.html"
    form_class = CreateAssetStatusForm

    def get_success_url(self):
        return reverse_lazy("asset:status_list")

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class AssetStatusUpdateView(LoginRequiredMixin, UpdateView):
    model = AssetStatus
    template_name = "asset/status/update.html"
    fields = (
        "name",
        "description",
    )

    success_url = reverse_lazy("asset:status_list")


class AssetStatusDeleteView(LoginRequiredMixin, DeleteView):
    model = AssetStatus
    template_name = "asset/status/delete.html"
    success_url = reverse_lazy("asset:status_list")
