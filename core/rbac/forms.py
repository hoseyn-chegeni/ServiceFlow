from django import forms
from django.contrib.auth.models import Permission

class PermissionForm(forms.Form):
    permissions = forms.ModelMultipleChoiceField(
        queryset=Permission.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label='Select Permissions'
    )