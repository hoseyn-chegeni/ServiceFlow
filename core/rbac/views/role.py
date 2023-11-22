from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    UpdateView,
    ListView,
    DetailView,
)
from ..models import Role, UserRole
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


class RoleListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Role
    template_name = "rbac/role/list.html"
    permission_required = "rbac.view_role"
    context_object_name = "role"


class RoleDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Role
    template_name = "rbac/role/detail.html"
    permission_required = "rbac.view_role"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["users"] = UserRole.objects.filter(role_id=self.kwargs["pk"])
        return context


class RoleCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Role
    template_name = "rbac/role/create.html"
    permission_required = "rbac.view_role"
    fields = (
        "name",
        "permissions",
    )

    def get_success_url(self):
        return reverse_lazy("rbac:role_list")

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class RoleUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Role
    template_name = "rbac/role/update.html"
    permission_required = "rbac.view_role"
    fields = (
        "name",
        "permissions",
        "is_active",
    )
    success_url = reverse_lazy("rbac:role_list")


class RoleDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Role
    template_name = "rbac/role/delete.html"
    permission_required = "rbac.view_role"
    success_url = reverse_lazy("rbac:role_list")
