from django.urls import reverse_lazy
from base.views import (
    BaseCreateView,
    BaseUpdateView,
    BaseDeleteView,
    BaseListView,
    BaseDetailView,
)
from ..models.accessory import Accessory, AccessoryCategory
from ..filters import AccessoryFilters, AccessoryCategoryFilters
from ..forms import CreateAccessoryForm, CreateAccessoryCategoryForm


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
    url = "asset:accessory_detail"


class AccessoryUpdateView(BaseUpdateView):
    model = Accessory
    template_name = "asset/accessory/update.html"
    permission_required = "asset.change_accessory"
    success_message = "Accessory Successfully Updated."
    fields = ("name",)
    url = "asset:accessory_detail"


class AccessoryDeleteView(BaseDeleteView):
    model = Accessory
    template_name = "asset/accessory/delete.html"
    success_url = reverse_lazy("asset:accessory_list")
    permission_required = "asset.delete_accessory"
    message = "Accessory Successfully Deleted"


# CATEGORY
# CATEGORY
# CATEGORY
# CATEGORY
# CATEGORY
# CATEGORY
# CATEGORY
# CATEGORY
# CATEGORY
# CATEGORY
# CATEGORY


class AccessoryCategoryListView(BaseListView):
    model = AccessoryCategory
    template_name = "asset/accessory_category/list.html"
    context_object_name = "accessory"
    filterset_class = AccessoryCategoryFilters
    permission_required = "asset.view_accessorycategory"


class AccessoryCategoryDetailView(BaseDetailView):
    model = AccessoryCategory
    template_name = "asset/accessory_category/detail.html"
    permission_required = "asset.view_accessorycategory"


class AccessoryCategoryCreateView(BaseCreateView):
    model = AccessoryCategory
    template_name = "asset/accessory_category/create.html"
    form_class = CreateAccessoryCategoryForm
    permission_required = "asset.add_accessorycategory"
    success_message = "Category Successfully Created."
    url = "asset:accessory_category_detail"

class AccessoryCategoryUpdateView(BaseUpdateView):
    model = AccessoryCategory
    template_name = "asset/accessory_category/update.html"
    permission_required = "asset.change_accessorycategory"
    success_message = "Category Successfully Updated."
    fields = ("name",)
    url= "asset:accessory_category_detail"


class AccessoryCategoryDeleteView(BaseDeleteView):
    model = AccessoryCategory
    template_name = "asset/accessory_category/delete.html"
    success_url = reverse_lazy("asset:accessory_category_list")
    permission_required = "asset.delete_accessorycategory"
    message = "Category Successfully Deleted"
