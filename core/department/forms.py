from django import forms
from .models import Department


class DepartmentCreateForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = (
            "name",
            "description",
            "manager",
            "active_status",
            "organization",
        )
