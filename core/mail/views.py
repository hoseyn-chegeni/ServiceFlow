from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.
class InboxView(TemplateView):
    template_name = 'mail/inbox.html'
