from django.urls import reverse
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import User
from .forms import UserCreationForm
# Create your views here.

class UserView(ListView):
    model = User


class UserLogin(LoginView):
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse('index:home')
    
class UserLogout(LogoutView):

    def get_success_url(self):
        return reverse('accounts:login')
    



class CreateUser(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('index:home')