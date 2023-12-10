from django.views.generic import DetailView

from ..models.license import License, LicenseCategory
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from base.views import BaseCreateView, BaseDeleteView, BaseListView, BaseUpdateView
from ..filters import LicenseFilters, LicenseCategoryFilters


# LICENSE Views Here...
class LicenseListView(BaseListView):
    model = License
    template_name = "asset/license/list.html"
    context_object_name = "license"
    permission_required = "asset.view_license"
    filterset_class = LicenseFilters


class LicenseDetailView(PermissionRequiredMixin, LoginRequiredMixin, DetailView):
    model = License
    template_name = "asset/license/detail.html"
    permission_required = "asset.view_license"


class LicenseCreateView(BaseCreateView):
    model = License
    template_name = "asset/license/create.html"
    fields = "__all__"
    permission_required = "asset.add_license"
    success_message = "License Successfully Created."

    def get_success_url(self):
        return reverse_lazy("asset:license_detail", kwargs={"pk": self.object.pk})


class LicenseUpdateView(BaseUpdateView):
    model = License
    template_name = "asset/license/update.html"
    fields = "__all__"
    permission_required = "asset.change_license"
    success_message = "License Successfully Updated"

    def get_success_url(self):
        return reverse_lazy("asset:license_detail", kwargs={"pk": self.object.pk})


class LicenseDeleteView(BaseDeleteView):
    model = License
    template_name = "asset/license/delete.html"
    success_url = reverse_lazy("asset:license_list")
    permission_required = "asset.delete_license"
    message = "License Successfully Deleted!"


# LICENSE CATEGORYCategory Views Here...
class LicenseCategoryListView(BaseListView):
    model = LicenseCategory
    template_name = "asset/license_category/list.html"
    context_object_name = "license"
    permission_required = "asset.view_licensecategory"
    filterset_class = LicenseCategoryFilters


class LicenseCategoryDetailView(
    PermissionRequiredMixin, LoginRequiredMixin, DetailView
):
    model = LicenseCategory
    template_name = "asset/license_category/detail.html"
    permission_required = "asset.view_licensecategory"


class LicenseCategoryCreateView(BaseCreateView):
    model = LicenseCategory
    template_name = "asset/license_category/create.html"
    fields = "__all__"
    permission_required = "asset.add_licensecategory"
    success_message = "License Category Successfully Created."

    def get_success_url(self):
        return reverse_lazy(
            "asset:license_category_detail", kwargs={"pk": self.object.pk}
        )


class LicenseCategoryUpdateView(BaseUpdateView):
    model = LicenseCategory
    template_name = "asset/license_category/update.html"
    fields = "__all__"
    permission_required = "asset.change_licensecategory"
    success_message = "License Category Successfully Updated."

    def get_success_url(self):
        return reverse_lazy(
            "asset:license_category_detail", kwargs={"pk": self.object.pk}
        )


class LicenseCategoryDeleteView(BaseDeleteView):
    model = LicenseCategory
    template_name = "asset/license_category/delete.html"
    success_url = reverse_lazy("asset:license_category_list")
    permission_required = "asset.delete_licensecategory"
    message = "License Category Successfully Created."
