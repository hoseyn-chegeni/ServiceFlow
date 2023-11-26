# from django.views.generic import (
#     DeleteView,
#     CreateView,
#     UpdateView,
#     DetailView,
#     ListView,
# )
# from django_filters.views import FilterView
# from ..models.license import License, LicenseCategory
# from django.urls import reverse_lazy
# from ..filters import ComponentFilters
# from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


# # Component Views Here...
# class ComponentListView(PermissionRequiredMixin, LoginRequiredMixin, FilterView):
#     model = Component
#     template_name = "asset/component/list.html"
#     filterset_class = ComponentFilters
#     context_object_name = "component"
#     permission_required = "asset.view_component"


# class ComponentDetailView(PermissionRequiredMixin, LoginRequiredMixin, DetailView):
#     model = Component
#     template_name = "asset/component/detail.html"
#     permission_required = "asset.view_component"


# class ComponentCreateView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
#     model = Component
#     template_name = "asset/component/create.html"
#     fields = "__all__"
#     permission_required = "asset.add_component"

#     def get_success_url(self):
#         return reverse_lazy("asset:component_list")

#     def form_valid(self, form):
#         form.instance.created_by = self.request.user
#         return super().form_valid(form)


# class ComponentUpdateView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
#     model = ComponentCategory
#     template_name = "asset/component/update.html"
#     fields = "__all__"
#     permission_required = "asset.change_component"
#     success_url = reverse_lazy("asset:component_list")


# class ComponentDeleteView(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
#     model = ComponentCategory
#     template_name = "asset/component/delete.html"
#     success_url = reverse_lazy("asset:component_list")
#     permission_required = "asset.delete_component"