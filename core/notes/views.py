from typing import Any
from django.shortcuts import render
from django.views.generic import ListView
from .models import Note
from django_filters.views import FilterView
from .filters import NoteFilter, PublicNoteFilter

# Create your views here.

class PublicNoteView(FilterView):
    template_name = 'notes/public_notes.html'
    model = Note
    context_object_name = 'notes'
    filterset_class = PublicNoteFilter
    def get_queryset(self, **kwargs):
       qs = super().get_queryset(**kwargs)
       return qs.filter(is_public=True, is_archive = False)

    

class MyNotesView(FilterView):
    template_name = 'notes/my_notes.html'
    model = Note
    filterset_class = NoteFilter
    context_object_name = 'notes'
    def get_queryset(self, **kwargs):
       qs = super().get_queryset(**kwargs)
       return qs.filter(author_id=self.request.user.id, is_archive = False)


class MyArchiveNotesView(FilterView):
    template_name = 'notes/my_archive_notes.html'
    model = Note
    context_object_name = 'notes'
    filterset_class = NoteFilter
    def get_queryset(self, **kwargs):
       qs = super().get_queryset(**kwargs)
       return qs.filter(author_id=self.request.user.id, is_archive = True)