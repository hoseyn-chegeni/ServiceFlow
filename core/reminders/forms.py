from django import forms
from .models import Reminder


class ReminderCreateForm(forms.ModelForm):
    class Meta:
        model = Reminder
        fields = ("title", "description", "date", "time", "assign_to", "is_completed")
