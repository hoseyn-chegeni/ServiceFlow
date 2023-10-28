from django.shortcuts import render
from .filters import TeamFilter
from django_filters.views import FilterView
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView
from .models import Team
from .forms import TeamCreteForm
from django.urls import reverse_lazy

# Create your views here.


class TeamView(FilterView):
    model = Team
    filterset_class = TeamFilter
    context_object_name = "team"
    template_name = "team/team.html"

    def get_queryset(self, **kwargs):
        qs = super().get_queryset(**kwargs)
        return qs.filter(is_active=True)


class TeamDetailView(DetailView):
    model = Team
    template_name = "team/detail.html"


class TeamUpdateView(UpdateView):
    model = Team
    template_name = "team/update.html"
    fields = (
        "name",
        "description",
        "members",
        "leader",
        "responsibilities",
        "is_active",
        "budget",
    )
    success_url = reverse_lazy("team:team_list")


class TeamCreateView(CreateView):
    model = Team
    template_name = "team/create.html"
    form_class = TeamCreteForm
    success_url = reverse_lazy("team:team_list")

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


class TeamDeleteView(DeleteView):
    model = Team
    template_name = "team/delete.html"
    success_url = reverse_lazy("team:team_list")
