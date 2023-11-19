from django.db.models.base import Model as Model
from django.urls import reverse, reverse_lazy
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.views.generic import ListView, UpdateView, DetailView, DeleteView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import User
from .forms import CustomUserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from tasks.models import Task
from db_events.models import TaskLog
from db_events.models import UserAuthenticationLog
import csv
from django.views import View
from dotenv import load_dotenv
from decouple import config

load_dotenv()


# Create your views here.


class UserView(LoginRequiredMixin, ListView):
    model = User
    template_name = "registration/user_list.html"

    def get_queryset(self, **kwargs):
        qs = super().get_queryset(**kwargs)
        return qs.filter(is_active=True)


class UserLogin(LoginView):
    redirect_authenticated_user = True

    def form_valid(self, form):
        # Log successful login
        response = super().form_valid(form)
        UserAuthenticationLog.objects.create(
            user=self.request.user,
            ip_address=self.request.META.get('REMOTE_ADDR'),
            status='Success'
        )
        return response

    def form_invalid(self, form):
        # Log failed login
        response = super().form_invalid(form)
        UserAuthenticationLog.objects.create(
            user=None,  # User is None for failed login attempts
            ip_address=self.request.META.get('REMOTE_ADDR'),
            status='Failure'
        )
        return response

    def get_success_url(self):
        return reverse("index:home")


class UserLogout( LogoutView):
    def get_success_url(self):
        return reverse("accounts:login")


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

    def get_object(self, queryset=None):
        return get_object_or_404(User, pk=self.kwargs.get('pk'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context['user_permissions'] = user.user_permissions.all()
        context['user_created_task'] = Task.objects.filter(creator_id = user.id).count()
        context['user_assigned_task'] = Task.objects.filter(assign_to_id = user.id).count()
        return context


class UserDelete(LoginRequiredMixin, DeleteView):
    model = User
    template_name = "registration/delete.html"
    success_url = reverse_lazy("accounts:users")


class UserPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    template_name = "registration/change_password.html"
    success_url = reverse_lazy("index:home")


class SuspendUserView(UpdateView):
    model = User
    fields = ('is_active',)
    template_name = 'registration/suspend_user.html'
    success_url = reverse_lazy('accounts:users')

    def form_valid(self, form):
        form.instance.is_active = False
        return super().form_valid(form)
    

class ReactiveUserView(UpdateView):
    model = User
    fields = ('is_active',)
    template_name = 'registration/reactive_user.html'
    success_url = reverse_lazy('accounts:suspended_list')

    def form_valid(self, form):
        form.instance.is_active = True
        return super().form_valid(form)
    

class SuspendUserListView(ListView):
    model = User
    template_name = 'registration/suspend_list.html'

    def get_queryset(self, **kwargs):
        qs = super().get_queryset(**kwargs)
        return qs.filter(is_active=False)
    

class UserActivitiesOnTasks(ListView):
    model = TaskLog
    template_name = 'registration/user_activities_on_tasks.html'
    context_object_name = 'log'
    def get_queryset(self):
        task = get_object_or_404(User, pk=self.kwargs["pk"])
        return task.user.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user"] = get_object_or_404(User, pk=self.kwargs["pk"])
        return context
    


class BulkUserImportView(View):
    template_name = 'registration/import_form.html'
    success_template_name = 'registration/import_success.html'
    error_template_name = 'registration/import_error.html'
    default_password = config("DEFAULT_PASSWORD")

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        if request.method == 'POST' and request.FILES.get('file'):
            file = request.FILES['file']
            if file.name.endswith('.csv'):
                users_added = 0
                decoded_file = file.read().decode('utf-8')
                csv_data = csv.reader(decoded_file.splitlines(), delimiter=',')
                for row in csv_data:
                    email = row[0]
                    first_name = row[1]
                    last_name = row[2]
                    user, created = User.objects.get_or_create(email=email, first_name=first_name,last_name = last_name)
                    if created:
                        user.set_password(self.default_password)  # Set default password
                        user.save()
                        users_added += 1
                
                return render(request, self.success_template_name, {'users_added': users_added})
            else:
                return render(request, self.error_template_name)
        return render(request, self.template_name)
