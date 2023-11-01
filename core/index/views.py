from typing import Any
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from accounts.models import User
from tasks.models import Task
from notes.models import Note
from meetings.models import Meetings


# Create your views here.
class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context["users"] = User.objects.all().count()
        context["tasks"] = Task.objects.all().count()
        context["notes"] = Note.objects.filter(is_public=True).count()
        context["has_team_permission"] = self.request.user.has_perm("team.view_team")
        context["has_notes_permission"] = self.request.user.has_perm("notes.view_note")
        context["meetings"] = Meetings.objects.filter(
            attendees=self.request.user
        ).count()
        return context
