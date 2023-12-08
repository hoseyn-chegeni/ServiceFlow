from django.views.generic import (
    DeleteView,
    CreateView,
    UpdateView,
    DetailView,
)
from ..models.consumable import ConsumableCategory, Consumable
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from ..filters import ConsumableFilters
from base.views import BaseListView, BaseDeleteView


# CONSUMABLE Views Here...
class ConsumableListView(BaseListView):
    model = Consumable
    template_name = "asset/consumable/list.html"
    context_object_name = "consumable"
    permission_required = "asset.view_consumable"
    filterset_class = ConsumableFilters


class ConsumableDetailView(PermissionRequiredMixin, LoginRequiredMixin, DetailView):
    model = Consumable
    template_name = "asset/consumable/detail.html"
    permission_required = "asset.view_consumable"


class ConsumableCreateView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    model = Consumable
    template_name = "asset/consumable/create.html"
    fields = "__all__"
    permission_required = "asset.add_consumable"

    def get_success_url(self):
        return reverse_lazy("asset:consumable_list")

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class ConsumableUpdateView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Consumable
    template_name = "asset/consumable/update.html"
    fields = "__all__"
    permission_required = "asset.change_consumable"
    success_url = reverse_lazy("asset:consumable_list")


class ConsumableDeleteView(BaseDeleteView):
    model = Consumable
    template_name = "asset/consumable/delete.html"
    success_url = reverse_lazy("asset:consumable_list")
    permission_required = "asset.delete_consumable"
    message = "Consumable Successfully Deleted"
