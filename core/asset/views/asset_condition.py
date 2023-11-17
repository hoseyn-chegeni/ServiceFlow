from django.views.generic import (
    ListView,
    DeleteView,
    CreateView,
    UpdateView,
    DetailView,
)
from ..models.asset_condition import AssetCondition
from django.urls import reverse_lazy
from ..forms import CreateAssetConditionForm
from django.contrib.auth.mixins import LoginRequiredMixin


class AssetConditionListView(LoginRequiredMixin, ListView):
    model = AssetCondition
    template_name = "asset/condition/list.html"
    context_object_name = "asset"


class AssetConditionDetailView(LoginRequiredMixin, DetailView):
    model = AssetCondition
    template_name = "asset/condition/detail.html"


class AssetConditionCreateView(LoginRequiredMixin, CreateView):
    model = AssetCondition
    template_name = "asset/condition/create.html"
    form_class = CreateAssetConditionForm

    def get_success_url(self):
        return reverse_lazy("asset:condition_list")

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class AssetConditionUpdateView(LoginRequiredMixin, UpdateView):
    model = AssetCondition
    template_name = "asset/condition/update.html"
    fields = (
        "name",
        "description",
    )

    success_url = reverse_lazy("asset:condition_list")


class AssetConditionDeleteView(LoginRequiredMixin, DeleteView):
    model = AssetCondition
    template_name = "asset/condition/delete.html"
    success_url = reverse_lazy("asset:condition_list")
