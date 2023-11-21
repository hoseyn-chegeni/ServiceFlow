import django_filters
from django_filters import FilterSet
from .models import UserRole


class UserRoleFilter(FilterSet):
    class Meta:
        model = UserRole
        fields = [
            "user",
            "role",
        ]
