from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import UserRole
from accounts.models import User
# Create your views here.

class AssignRoleToUser(CreateView):
    model = UserRole
    fields = ['role',]
    template_name = 'rbac/assign_role_to_user.html'
    success_url = reverse_lazy('accounts:users')
    def form_valid(self, form):
        user = get_object_or_404(User, pk = self.kwargs["pk"])
        form.instance.user = user
        return super().form_valid(form)
    
