from typing import Any
from django.db.models.base import Model as Model
from django.urls import reverse, reverse_lazy
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.views.generic import ListView, UpdateView, DetailView, DeleteView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import User
from .forms import CustomUserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from tasks.models import Task
from db_events.models import TaskLog
from db_events.models import UserAuthenticationLog
import csv
from django.views import View
from dotenv import load_dotenv
from decouple import config
from django_otp.forms import OTPAuthenticationForm
from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)
from django_filters.views import FilterView
from .filters import UserFilter
from django.http import HttpResponseRedirect


load_dotenv()


# Create your views here.


class UserView(LoginRequiredMixin, PermissionRequiredMixin, FilterView):
    model = User
    template_name = "registration/user_list.html"
    permission_required = "accounts.view_user"
    filterset_class = UserFilter
    context_object_name = 'users'

    def get_queryset(self, **kwargs):
        qs = super().get_queryset(**kwargs)
        return qs.filter(is_active=True)
    
    def get_paginate_by(self, queryset):
        # Get the value for paginate_by dynamically (e.g., from a form input or session)
        # Example: Set paginate_by to a user-selected value stored in session
        user_selected_value = self.request.session.get('items_per_page', 10)  # Default to 10
        return user_selected_value

class UserLogin(LoginView):
    redirect_authenticated_user = True
    authentication_form = OTPAuthenticationForm

    def form_valid(self, form):
        # Log successful login
        response = super().form_valid(form)
        UserAuthenticationLog.objects.create(
            user=self.request.user,
            ip_address=self.request.META.get("REMOTE_ADDR"),
            status="Success",
        )
        return response

    def form_invalid(self, form):
        # Log failed login
        response = super().form_invalid(form)
        UserAuthenticationLog.objects.create(
            user=None,  # User is None for failed login attempts
            ip_address=self.request.META.get("REMOTE_ADDR"),
            status="Failure",
        )
        return response

    def get_success_url(self):
        return reverse("index:home")


class UserLogout(LogoutView):
    def get_success_url(self):
        return reverse("two_factor:login")


class CreateUser(LoginRequiredMixin, CreateView):
    model = User
    form_class = CustomUserCreationForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("index:home")


class UserUpdate(LoginRequiredMixin, UpdateView):
    model = User
    fields = ("first_name", "last_name", "image")
    template_name = "registration/update.html"
    success_url = reverse_lazy("accounts:users")


class UserDetail(LoginRequiredMixin, DetailView):
    model = User
    template_name = "registration/detail.html"
    context_object_name = 'user'
    def get_object(self, queryset=None):
        return get_object_or_404(User, pk=self.kwargs.get("pk"))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context["user_permissions"] = user.user_permissions.all()
        context["user_created_task"] = Task.objects.filter(creator_id=user.id).count()
        context["user_assigned_task"] = Task.objects.filter(
            assign_to_id=user.id
        ).count()
        return context


class UserDelete(LoginRequiredMixin, DeleteView):
    model = User
    template_name = "registration/delete.html"
    success_url = reverse_lazy("accounts:users")
    def get(self, request, *args, **kwargs):
        # Get the object to be deleted
        self.object = self.get_object()

        # Perform the delete operation directly without displaying a confirmation template
        success_url = self.get_success_url()
        self.object.delete()
        return HttpResponseRedirect(success_url)


class UserPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    template_name = "registration/change_password.html"
    success_url = reverse_lazy("index:home")


class SuspendUserView(View):
    def get(self, request, pk):
        user = User.objects.filter(pk=pk).first()  # Get the user object
        if user:
            user.is_active = False  # Activate the user
            user.save()
        return HttpResponseRedirect(reverse_lazy('accounts:users')) 


class ReactiveUserView(UpdateView):
    model = User
    fields = ("is_active",)
    template_name = "registration/reactive_user.html"
    success_url = reverse_lazy("accounts:suspended_list")

    def form_valid(self, form):
        form.instance.is_active = True
        return super().form_valid(form)


class SuspendUserListView(FilterView):
    model = User
    template_name = "registration/suspend_list.html"
    filterset_class = UserFilter
    context_object_name = 'users'

    def get_queryset(self, **kwargs):
        qs = super().get_queryset(**kwargs)
        return qs.filter(is_active=False)
    
    def get_paginate_by(self, queryset):
        user_selected_value = self.request.session.get('items_per_page', 10) 
        return user_selected_value


class UserActivitiesOnTasks(ListView):
    model = TaskLog
    template_name = "registration/user_activities_on_tasks.html"
    context_object_name = "log"

    def get_queryset(self):
        task = get_object_or_404(User, pk=self.kwargs["pk"])
        return task.user.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user"] = get_object_or_404(User, pk=self.kwargs["pk"])
        return context


class BulkUserImportView(View):
    template_name = "registration/import_form.html"
    success_template_name = "registration/import_success.html"
    error_template_name = "registration/import_error.html"
    default_password = config("DEFAULT_PASSWORD")

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        if request.method == "POST" and request.FILES.get("file"):
            file = request.FILES["file"]
            if file.name.endswith(".csv"):
                users_added = 0
                decoded_file = file.read().decode("utf-8")
                csv_data = csv.reader(decoded_file.splitlines(), delimiter=",")
                for row in csv_data:
                    email = row[0]
                    first_name = row[1]
                    last_name = row[2]
                    user, created = User.objects.get_or_create(
                        email=email, first_name=first_name, last_name=last_name
                    )
                    if created:
                        user.set_password(self.default_password)  # Set default password
                        user.save()
                        users_added += 1

                return render(
                    request, self.success_template_name, {"users_added": users_added}
                )
            else:
                return render(request, self.error_template_name)
        return render(request, self.template_name)


class CustomPasswordResetView(PasswordResetView):
    template_name = "registration/forgot_password/password_reset.html"
    email_template_name = "registration/forgot_password/password_reset_email.html"
    success_url = reverse_lazy("accounts:password_reset_done")


class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = "registration/forgot_password/password_reset_done.html"


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = "registration/forgot_password/password_reset_confirm.html"
    success_url = reverse_lazy("accounts:password_reset_complete")


class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = "registration/forgot_password/password_reset_complete.html"
