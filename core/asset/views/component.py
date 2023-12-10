from django.views.generic import (
    CreateView,
    UpdateView,
    DetailView,
)
from ..models.component import Component, ComponentCategory
from django.urls import reverse_lazy
from ..filters import ComponentFilters, ComponentCategoryFilters
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from base.views import (
    BaseDeleteView,
    BaseListView,
    BaseCreateView,
    BaseDetailView,
    BaseUpdateView,
)


# Component Views Here...
class ComponentListView(BaseListView):
    model = Component
    template_name = "asset/component/list.html"
    filterset_class = ComponentFilters
    context_object_name = "component"
    permission_required = "asset.view_component"


class ComponentDetailView(BaseDetailView):
    model = Component
    template_name = "asset/component/detail.html"
    permission_required = "asset.view_component"


class ComponentCreateView(BaseCreateView):
    model = Component
    template_name = "asset/component/create.html"
    fields = "__all__"
    permission_required = "asset.add_component"
    url = "asset:component_detail"
    success_message = "Component Successfully Created."


class ComponentUpdateView(BaseUpdateView):
    model = Component
    template_name = "asset/component/update.html"
    fields = "__all__"
    permission_required = "asset.change_component"
    url = "asset:component_detail"
    success_message = "Component Successfully Updated."


class ComponentDeleteView(BaseDeleteView):
    model = Component
    template_name = "asset/component/delete.html"
    success_url = reverse_lazy("asset:component_list")
    permission_required = "asset.delete_component"
    message = "Component successfully Deleted!"


# Component Category Views Here...


class ComponentCategoryListView(BaseListView):
    model = ComponentCategory
    template_name = "asset/component_category/list.html"
    context_object_name = "component"
    permission_required = "asset.view_componentcategory"
    filterset_class = ComponentCategoryFilters


class ComponentCategoryDetailView(BaseDetailView):
    model = ComponentCategory
    template_name = "asset/component_category/detail.html"
    permission_required = "asset.view_componentcategory"


class ComponentCategoryCreateView(BaseCreateView):
    model = ComponentCategory
    template_name = "asset/component_category/create.html"
    fields = "__all__"
    permission_required = "asset.add_componentcategory"
    success_message = "Component Successfully Created."
    url = "asset:component_category_detail"


class ComponentCategoryUpdateView(BaseUpdateView):
    model = ComponentCategory
    template_name = "asset/component_category/update.html"
    fields = "__all__"
    permission_required = "asset.change_componentcategory"
    url = "asset:component_category_detail"
    success_message = "Component Category Successfully updated."


class ComponentCategoryDeleteView(BaseDeleteView):
    model = ComponentCategory
    template_name = "asset/component_category/delete.html"
    success_url = reverse_lazy("asset:component_category_list")
    permission_required = "asset.delete_componentcategory"
    message = "Component Category Successfully Deleted!"
