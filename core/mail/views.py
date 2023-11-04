from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import Mail

# Create your views here.
class InboxView(TemplateView):
    template_name = 'mail/inbox.html'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['inbox'] = Mail.objects.filter(recipient = self.request.user)
        return context
