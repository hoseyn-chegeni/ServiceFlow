from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import  CreateView
from django_filters.views import FilterView
from ..filters import UserRoleFilter
from ..models import UserRole
from accounts.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

# Create your views here.


class AssignRoleToUser(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = UserRole
    fields = [
        "role",
    ]
    template_name = "rbac/assign_role_to_user.html"
    success_url = reverse_lazy("accounts:users")
    permission_required = "rbac.add_userrole"

    def form_valid(self, form):
        user = get_object_or_404(User, pk=self.kwargs["pk"])
        form.instance.user = user
        return super().form_valid(form)
    

class UserRolesListView(LoginRequiredMixin, PermissionRequiredMixin, FilterView):
    model= UserRole
    filterset_class = UserRoleFilter
    template_name = 'rbac/user_role_list.html'
    context_object_name = 'role'
    permission_required = "rbac.view_userrole"


