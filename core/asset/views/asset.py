from django.views.generic import DeleteView, CreateView, UpdateView, DetailView
from django_filters.views import FilterView
from ..models.asset import Asset
from django.urls import reverse_lazy
from ..forms import CreateAssetForm
from ..filters import AssetFilters


class AssetListView(FilterView):
    model = Asset
    template_name = "asset/list.html"
    filterset_class = AssetFilters
    context_object_name = "asset"


class AssetDetailView(DetailView):
    model = Asset
    template_name = "asset/detail.html"


class AssetCreateView(CreateView):
    model = Asset
    template_name = "asset/create.html"
    form_class = CreateAssetForm

    def get_success_url(self):
        return reverse_lazy("asset:list")

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class AssetUpdateView(UpdateView):
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
        "condition",
        "maintenance_schedule",
        "purchase_cost",
        "depreciation_rate",
        "assigned_ip_address",
        "software_installed",
        "notes",
    )

    success_url = reverse_lazy('asset:list')


class AssetDeleteView(DeleteView):
    model = Asset
    template_name = "asset/delete.html"
    success_url = reverse_lazy("asset:list")
