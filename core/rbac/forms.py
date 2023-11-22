from django import forms
from django.contrib.auth.models import Permission
from accounts.models import User

class PermissionForm(forms.Form):
    permissions = forms.ModelMultipleChoiceField(
        queryset=Permission.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label="Select Permissions",
    )





class AddUserToGroupForm(forms.Form):
    user = forms.ModelChoiceField(
        queryset=User.objects.all(),
        label='Select User to Add to Group'
    )