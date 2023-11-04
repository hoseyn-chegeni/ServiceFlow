from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from .models import Mail


# Create your views here.
class MailBoxView(CreateView ):
    template_name = 'mail/mail_box.html'
    model = Mail
    fields = ['recipient','subject','body',]
    success_url = reverse_lazy('mail:inbox')

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['inbox_counter'] =  Mail.objects.filter(recipient = self.request.user).count()
        context['inbox'] = Mail.objects.filter(recipient = self.request.user)
        return context
    
    def form_valid(self, form):
        form.instance.sender = self.request.user
        form.instance.folder = 'INBOX'
        return super().form_valid(form)