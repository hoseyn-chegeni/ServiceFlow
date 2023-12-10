from django.views.generic import (
    DeleteView,
    CreateView,
    UpdateView,
    DetailView,
)
from ..models.consumable import ConsumableCategory, Consumable
from django.urls import reverse_lazy
from ..filters import ConsumableFilters
from base.views import BaseListView, BaseDeleteView, BaseCreateView,BaseDetailView,BaseUpdateView


# CONSUMABLE Views Here...
class ConsumableListView(BaseListView):
    model = Consumable
    template_name = "asset/consumable/list.html"
    context_object_name = "consumable"
    permission_required = "asset.view_consumable"
    filterset_class = ConsumableFilters


class ConsumableDetailView(BaseDetailView):
    model = Consumable
    template_name = "asset/consumable/detail.html"
    permission_required = "asset.view_consumable"


class ConsumableCreateView(BaseCreateView):
    model = Consumable
    template_name = "asset/consumable/create.html"
    fields = "__all__"
    permission_required = "asset.add_consumable"
    success_message = 'Consumable Successfully Created.'

    def get_success_url(self):
        return reverse_lazy("asset:consumable_list")



class ConsumableUpdateView(BaseUpdateView):
    model = Consumable
    template_name = "asset/consumable/update.html"
    fields = "__all__"
    permission_required = "asset.change_consumable"
    success_url = reverse_lazy("asset:consumable_list")
    success_message = 'Consumable Successfully Created.'


class ConsumableDeleteView(BaseDeleteView):
    model = Consumable
    template_name = "asset/consumable/delete.html"
    success_url = reverse_lazy("asset:consumable_list")
    permission_required = "asset.delete_consumable"
    message = "Consumable Successfully Deleted"
