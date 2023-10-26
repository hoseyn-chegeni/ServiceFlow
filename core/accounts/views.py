from django.urls import reverse
from django.contrib.auth.views import LoginView, LogoutView

# Create your views here.


class UserLogin(LoginView):
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse('index:home')
    
class UserLogout(LogoutView):

    def get_success_url(self):
        return reverse('accounts:login')