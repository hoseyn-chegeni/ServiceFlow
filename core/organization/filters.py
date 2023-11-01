import django_filters
from django_filters import FilterSet
from .models import Organization


class OrganizationFilters(FilterSet):
    name = django_filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = Organization
        fields = [
            "id",
            "name",
            "phone_number",
            "email",
            "industry",
            "parent_organization",
            "legal_entity_type",
            "tax_id_number",
            "registration_number",
        ]
