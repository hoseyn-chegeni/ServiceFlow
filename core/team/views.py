from django.shortcuts import render
from .filters import TeamFilter
from django_filters.views import FilterView
from .models import Team

# Create your views here.


class TeamView(FilterView):
    model = Team
    filterset_class = TeamFilter
    context_object_name = "team"
    template_name = "team/team.html"

    def get_queryset(self, **kwargs):
        qs = super().get_queryset(**kwargs)
        return qs.filter(is_active=True)
