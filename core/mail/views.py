from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from .models import Mail
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class MailBoxView(LoginRequiredMixin, CreateView):
    template_name = "mail/mail_box.html"
    model = Mail
    fields = [
        "recipient",
        "subject",
        "body",
    ]
    success_url = reverse_lazy("mail:inbox")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["inbox_counter"] = Mail.objects.filter(
            recipient=self.request.user
        ).count()
        context["inbox"] = Mail.objects.filter(recipient=self.request.user)
        return context

    def form_valid(self, form):
        form.instance.sender = self.request.user
        form.instance.folder = "INBOX"
        return super().form_valid(form)


class SentItemView(LoginRequiredMixin, ListView):
    model = Mail
    template_name = "mail/sent.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["sent"] = Mail.objects.filter(sender=self.request.user)
        return context
