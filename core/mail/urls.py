from django.urls import path
from .views import MailBoxView
app_name = 'mail'

urlpatterns = [
    path('inbox/',MailBoxView.as_view(), name='inbox'),

]