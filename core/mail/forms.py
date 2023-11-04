from django import forms
from .models import Mail


class ComposeMailForm(forms.ModelForm):
    class Meta:
        model = Mail
        fields = (
            "recipient",
            "body",
            "attachments",
        )
