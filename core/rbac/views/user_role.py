from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    UpdateView,
    ListView,
    DetailView,
)
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
