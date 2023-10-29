from django.urls import reverse, reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.views.generic import ListView, UpdateView, DetailView, DeleteView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import User
from .forms import UserCreationForm

# Create your views here.


class UserView(ListView):
    model = User
    template_name = "registration/user_list.html"


class UserLogin(LoginView):
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse("index:home")


class UserLogout(LogoutView):
    def get_success_url(self):
        return reverse("accounts:login")


class CreateUser(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("index:home")


class UserUpdate(UpdateView):
    model = User
    fields = ("first_name", "last_name", "image")
    template_name = "registration/update.html"
    success_url = reverse_lazy("accounts:users")


class UserDetail(DetailView):
    model = User
    template_name = "registration/detail.html"


class UserDelete(DeleteView):
    model = User
    template_name = "registration/delete.html"
    success_url = reverse_lazy("accounts:users")


class UserPasswordChangeView(PasswordChangeView):
    template_name = "registration/change_password.html"
    success_url = reverse_lazy("index:home")
