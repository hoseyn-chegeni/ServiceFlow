from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView
from django_filters.views import FilterView
from ..filters import UserRoleFilter
from ..models import UserRole
from accounts.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import Group
from ..forms import AddUserToGroupForm
# Create your views here.


class AssignRoleToUser(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = User
    fields = ('member_of',)
    template_name = "rbac/assign_role_to_user.html"
    permission_required = 'auth.change_group'  # Permission required to add users to group
    success_url = reverse_lazy("accounts:users")# Replace 'group_list' with your actual URL name

    def form_valid(self, form):
        group = form.instance.member_of
        user = get_object_or_404(User, id=self.kwargs['pk'])
        user.groups.add(group)
        return super().form_valid(form)


class UserRolesListView(LoginRequiredMixin, PermissionRequiredMixin, FilterView):
    model = UserRole
    filterset_class = UserRoleFilter
    template_name = "rbac/user_role_list.html"
    context_object_name = "role"
    permission_required = "rbac.view_userrole"


class UserRoleDeleteFromProfile(
    LoginRequiredMixin, PermissionRequiredMixin, DeleteView
):
    model = UserRole
    permission_required = "rbac.delete_userrole"
    template_name = "rbac/delete.html"

    def get_success_url(self):
        user_role = self.get_object()
        user_id = user_role.user.pk
        return reverse_lazy("accounts:detail", kwargs={"pk": user_id})


class UserRoleDeleteFromRoleDetail(
    LoginRequiredMixin, PermissionRequiredMixin, DeleteView
):
    model = UserRole
    permission_required = "rbac.delete_userrole"
    template_name = "rbac/delete.html"

    def get_success_url(self):
        user_role = self.get_object()
        role_id = user_role.role.pk
        return reverse_lazy("rbac:role_detail", kwargs={"pk": role_id})
