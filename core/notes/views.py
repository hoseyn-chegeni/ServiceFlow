from django.shortcuts import render
from django.views.generic import ListView
from .models import Note
# Create your views here.

class PublicNoteView(ListView):
    template_name = 'notes/publicNotes.html'
    model = Note
    context_object_name = 'notes'
    def get_queryset(self, **kwargs):
       qs = super().get_queryset(**kwargs)
       return qs.filter(is_public=True)