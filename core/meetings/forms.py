from django import forms
from .models import Meetings


class CreateMeetingsForm(forms.ModelForm):
    class Meta:
        model = Meetings
        fields = ("title","description", "date_time","duration","location", "attendees","action")