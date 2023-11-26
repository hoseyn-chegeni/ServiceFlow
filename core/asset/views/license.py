from django.views.generic import (
    DeleteView,
    CreateView,
    UpdateView,
    DetailView,
    ListView,
)
from ..models.license import License, LicenseCategory
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


# LICENSE Views Here...
class LicenseListView(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    model = License
    template_name = "asset/license/list.html"
    context_object_name = "license"
    permission_required = "asset.view_license"


class LicenseDetailView(PermissionRequiredMixin, LoginRequiredMixin, DetailView):
    model = License
    template_name = "asset/license/detail.html"
    permission_required = "asset.view_license"


class LicenseCreateView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    model = License
    template_name = "asset/license/create.html"
    fields = "__all__"
    permission_required = "asset.add_license"

    def get_success_url(self):
        return reverse_lazy("asset:license_list")

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class LicenseUpdateView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    model = License
    template_name = "asset/license/update.html"
    fields = "__all__"
    permission_required = "asset.change_license"
    success_url = reverse_lazy("asset:license_list")


class LicenseDeleteView(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = License
    template_name = "asset/license/delete.html"
    success_url = reverse_lazy("asset:license_list")
    permission_required = "asset.delete_license"