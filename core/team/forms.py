from django import forms
from .models import Team


class TeamCreteForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = (
            "name",
            "description",
            "leader",
            "responsibilities",
            "is_active",
            "budget",
        )
