from django.urls import reverse_lazy
from base.views import (
    BaseCreateView,
    BaseUpdateView,
    BaseDeleteView,
    BaseListView,
    BaseDetailView,
)
from ..models.accessory import Accessory
from ..filters import AccessoryFilters
from ..forms import CreateAccessoryForm


class AccessoryListView(BaseListView):
    model = Accessory
    template_name = "asset/accessory/list.html"
    context_object_name = "accessory"
    filterset_class = AccessoryFilters
    permission_required = "asset.view_accessory"


class AccessoryDetailView(BaseDetailView):
    model = Accessory
    template_name = "asset/accessory/detail.html"
    permission_required = "asset.view_accessory"


class AccessoryCreateView(BaseCreateView):
    model = Accessory
    template_name = "asset/accessory/create.html"
    form_class = CreateAccessoryForm
    permission_required = "asset.add_accessory"
    success_message = "Accessory Successfully Created."

    def get_success_url(self):
        return reverse_lazy("asset:accessory_detail", kwargs={"pk": self.object.pk})


class AccessoryUpdateView(BaseUpdateView):
    model = Accessory
    template_name = "asset/accessory/update.html"
    permission_required = "asset.change_accessory"
    success_message = "Accessory Successfully Updated."
    fields = (
        "name",
    )

    def get_success_url(self):
        return reverse_lazy("asset:accessory_detail", kwargs={"pk": self.object.pk})


class AccessoryDeleteView(BaseDeleteView):
    model = Accessory
    template_name = "asset/accessory/delete.html"
    success_url = reverse_lazy("asset:accessory_list")
    permission_required = "asset.delete_accessory"
    message = "Accessory Successfully Deleted"
