from django.shortcuts import render
from django.views.generic import ListView
from .models import Note
# Create your views here.

class PublicNoteView(ListView):
    template_name = 'notes/public_notes.html'
    model = Note
    context_object_name = 'notes'
    def get_queryset(self, **kwargs):
       qs = super().get_queryset(**kwargs)
       return qs.filter(is_public=True)
    

class MyNotesView(ListView):
    template_name = 'notes/my_notes.html'
    model = Note
    context_object_name = 'notes'
    def get_queryset(self, **kwargs):
       qs = super().get_queryset(**kwargs)
       return qs.filter(author_id=self.request.user.id, is_archive = False)

class MyArchiveNotesView(ListView):
    template_name = 'notes/my_archive_notes.html'
    model = Note
    context_object_name = 'notes'
    def get_queryset(self, **kwargs):
       qs = super().get_queryset(**kwargs)
       return qs.filter(author_id=self.request.user.id, is_archive = True)