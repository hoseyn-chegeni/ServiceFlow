from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    UpdateView,
    ListView,
    DetailView,
)
from ..models import UserRole
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import Group
from accounts.models import User


class RoleListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Group
    template_name = "rbac/role/list.html"
    permission_required = "rbac.view_role"
    context_object_name = "role"


class RoleDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Group
    template_name = "rbac/role/detail.html"
    permission_required = "rbac.view_role"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["users"] = User.objects.filter(groups=self.kwargs["pk"])
        return context


class RoleCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Group
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
    model = Group
    template_name = "rbac/role/update.html"
    permission_required = "rbac.view_role"
    fields = "__all__"
    success_url = reverse_lazy("rbac:role_list")


class RoleDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Group
    template_name = "rbac/role/delete.html"
    permission_required = "rbac.view_role"
    success_url = reverse_lazy("rbac:role_list")
