from ..models.consumable import ConsumableCategory, Consumable
from django.urls import reverse_lazy
from ..filters import ConsumableFilters, ConsumableCategoryFilters
from base.views import (
    BaseListView,
    BaseDeleteView,
    BaseCreateView,
    BaseDetailView,
    BaseUpdateView,
)


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
    success_message = "Consumable Successfully Created."
    url = "asset:consumable_detail"


class ConsumableUpdateView(BaseUpdateView):
    model = Consumable
    template_name = "asset/consumable/update.html"
    fields = "__all__"
    permission_required = "asset.change_consumable"
    url = "asset:consumable_detail"
    success_message = "Consumable Successfully Created."


class ConsumableDeleteView(BaseDeleteView):
    model = Consumable
    template_name = "asset/consumable/delete.html"
    success_url = reverse_lazy("asset:consumable_list")
    permission_required = "asset.delete_consumable"
    message = "Consumable Successfully Deleted"


# CONSUMABLE CATEGORY
# CONSUMABLE CATEGORY
# CONSUMABLE CATEGORY
# CONSUMABLE CATEGORY
# CONSUMABLE CATEGORY


class ConsumableCategoryListView(BaseListView):
    model = ConsumableCategory
    template_name = "asset/consumable_category/list.html"
    context_object_name = "consumable"
    permission_required = "asset.view_consumablecategory"
    filterset_class = ConsumableCategoryFilters


class ConsumableCategoryDetailView(BaseDetailView):
    model = ConsumableCategory
    template_name = "asset/consumable_category/detail.html"
    permission_required = "asset.view_consumablecategory"


class ConsumableCategoryCreateView(BaseCreateView):
    model = ConsumableCategory
    template_name = "asset/consumable_category/create.html"
    fields = ['name','description','is_active',]
    permission_required = "asset.add_consumablecategory"
    success_message = "Category Successfully Created."
    url = "asset:consumable_category_detail"


class ConsumableCategoryUpdateView(BaseUpdateView):
    model = ConsumableCategory
    template_name = "asset/consumable_category/update.html"
    fields = ['name','description','is_active',]
    permission_required = "asset.change_consumablecategory"
    url = "asset:consumable_category_detail"
    success_message = "Category Successfully Created."


class ConsumableCategoryDeleteView(BaseDeleteView):
    model = ConsumableCategory
    template_name = "asset/consumable_category/delete.html"
    success_url = reverse_lazy("asset:consumable_category_list")
    permission_required = "asset.delete_consumablecategory"
    message = "Category Successfully Deleted"
