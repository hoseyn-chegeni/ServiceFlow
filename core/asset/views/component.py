from django.views.generic import (
    DeleteView,
    CreateView,
    UpdateView,
    DetailView,
    ListView,
)
from django_filters.views import FilterView
from ..models.component import Component, ComponentCategory
from django.urls import reverse_lazy
from ..filters import ComponentFilters
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


# Component Views Here...
class ComponentListView(PermissionRequiredMixin, LoginRequiredMixin, FilterView):
    model = Component
    template_name = "asset/component/list.html"
    filterset_class = ComponentFilters
    context_object_name = "component"
    permission_required = "asset.view_component"

    def get_paginate_by(self, queryset):
        # Get the value for paginate_by dynamically (e.g., from a form input or session)
        # Example: Set paginate_by to a user-selected value stored in session
        user_selected_value = self.request.session.get(
            "items_per_page", 10
        )  # Default to 10
        return user_selected_value


class ComponentDetailView(PermissionRequiredMixin, LoginRequiredMixin, DetailView):
    model = Component
    template_name = "asset/component/detail.html"
    permission_required = "asset.view_component"


class ComponentCreateView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    model = Component
    template_name = "asset/component/create.html"
    fields = "__all__"
    permission_required = "asset.add_component"

    def get_success_url(self):
        return reverse_lazy("asset:component_list")

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class ComponentUpdateView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Component
    template_name = "asset/component/update.html"
    fields = "__all__"
    permission_required = "asset.change_component"
    success_url = reverse_lazy("asset:component_list")


class ComponentDeleteView(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Component
    template_name = "asset/component/delete.html"
    success_url = reverse_lazy("asset:component_list")
    permission_required = "asset.delete_component"


# Component Category Views Here...


class ComponentCategoryListView(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    model = ComponentCategory
    template_name = "asset/component_category/list.html"
    context_object_name = "component"
    permission_required = "asset.view_componentcategory"


class ComponentCategoryDetailView(
    PermissionRequiredMixin, LoginRequiredMixin, DetailView
):
    model = ComponentCategory
    template_name = "asset/component_category/detail.html"
    permission_required = "asset.view_componentcategory"


class ComponentCategoryCreateView(
    PermissionRequiredMixin, LoginRequiredMixin, CreateView
):
    model = ComponentCategory
    template_name = "asset/component_category/create.html"
    fields = "__all__"
    permission_required = "asset.add_componentcategory"

    def get_success_url(self):
        return reverse_lazy("asset:component_category_list")

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class ComponentCategoryUpdateView(
    PermissionRequiredMixin, LoginRequiredMixin, UpdateView
):
    model = ComponentCategory
    template_name = "asset/component_category/update.html"
    fields = "__all__"
    permission_required = "asset.change_componentcategory"
    success_url = reverse_lazy("asset:component_category_list")


class ComponentCategoryDeleteView(
    PermissionRequiredMixin, LoginRequiredMixin, DeleteView
):
    model = ComponentCategory
    template_name = "asset/component_category/delete.html"
    success_url = reverse_lazy("asset:component_category_list")
    permission_required = "asset.delete_componentcategory"
