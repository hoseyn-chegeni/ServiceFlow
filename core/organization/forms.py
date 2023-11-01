from django import forms
from .models import Organization


class OrganizationCreateForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = (
            "name",
            "address",
            "postal_code",
            "phone_number",
            "email",
            "industry",
            "employee_count",
            "founding_date",
            "parent_organization",
            "subsidiaries",
            "legal_entity_type",
            "tax_id_number",
            "registration_number",
            "registration_date",
            "logo",
        )
