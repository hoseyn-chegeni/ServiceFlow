from django.urls import path
from .models import Mail
from .views import InboxView
app_name = 'mail'

urlpatterns = [
    path('inbox/',InboxView.as_view(), name='inbox')
    
]