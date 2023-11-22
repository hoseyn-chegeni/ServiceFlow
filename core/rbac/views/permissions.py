from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    UpdateView,
    ListView,
    DetailView,
)
from django.contrib.auth.models import Permission
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from accounts.models import User
from ..forms import PermissionForm


class PermissionListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Permission
    template_name = "rbac/permission/list.html"
    permission_required = "permission.view_permission"
    context_object_name = "permission"
    ordering = ["id"]


class PermissionDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Permission
    template_name = "rbac/permission/detail.html"
    permission_required = "rbac.view_permission"


class PermissionUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Permission
    template_name = "rbac/permission/update.html"
    permission_required = "permission.change_permission"
    fields = ("__all__")
    def get_success_url(self):
        return reverse_lazy('rbac:permission_detail',kwargs={"pk": self.kwargs['pk']})
    

class PermissionCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Permission
    template_name = "rbac/permission/create.html"
    permission_required = "permission.add_permission"
    fields = ("__all__")
    def get_success_url(self):
        return reverse_lazy('rbac:permission_list')
    

class PermissionDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Permission
    template_name = "rbac/permission/delete.html"
    permission_required = "permission.delete_permission"
    def get_success_url(self):
        return reverse_lazy('rbac:permission_list')
    

class AssignPermissionView(LoginRequiredMixin, PermissionRequiredMixin,UpdateView):
    model = User
    fields = ("user_permissions",)
    template_name = 'rbac/permission/assign_permission.html'
    permission_required = 'auth.change_user'

    def get_success_url(self):
        user = self.get_object()
        return reverse_lazy('accounts:detail', kwargs={"pk": user.id})
