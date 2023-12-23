from django.views.generic import DetailView

from ..models.license import License, LicenseCategory
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from base.views import (
    BaseCreateView,
    BaseDeleteView,
    BaseListView,
    BaseUpdateView,
    BaseDetailView,
)
from ..filters import LicenseFilters, LicenseCategoryFilters


# LICENSE Views Here...
class LicenseListView(BaseListView):
    model = License
    template_name = "asset/license/list.html"
    context_object_name = "license"
    permission_required = "asset.view_license"
    filterset_class = LicenseFilters


class LicenseDetailView(BaseDetailView):
    model = License
    template_name = "asset/license/detail.html"
    permission_required = "asset.view_license"


class LicenseCreateView(BaseCreateView):
    model = License
    template_name = "asset/license/create.html"
    fields = "__all__"
    permission_required = "asset.add_license"
    success_message = "License Successfully Created."
    url = "asset:license_detail"


class LicenseUpdateView(BaseUpdateView):
    model = License
    template_name = "asset/license/update.html"
    fields = "__all__"
    permission_required = "asset.change_license"
    success_message = "License Successfully Updated"
    url = "asset:license_detail"


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


class LicenseCategoryDetailView(BaseDetailView):
    model = LicenseCategory
    template_name = "asset/license_category/detail.html"
    permission_required = "asset.view_licensecategory"
    context_object_name = 'license_category'


class LicenseCategoryCreateView(BaseCreateView):
    model = LicenseCategory
    template_name = "asset/license_category/create.html"
    fields = ['name','description','is_active',]
    permission_required = "asset.add_licensecategory"
    success_message = "License Category Successfully Created."
    url = "asset:license_category_detail"


class LicenseCategoryUpdateView(BaseUpdateView):
    model = LicenseCategory
    template_name = "asset/license_category/update.html"
    fields = ['name','description','is_active',]
    permission_required = "asset.change_licensecategory"
    success_message = "License Category Successfully Updated."
    url = "asset:license_category_detail"
    context_object_name = 'license_category'


class LicenseCategoryDeleteView(BaseDeleteView):
    model = LicenseCategory
    template_name = "asset/license_category/delete.html"
    success_url = reverse_lazy("asset:license_category_list")
    permission_required = "asset.delete_licensecategory"
    message = "License Category Successfully Created."
