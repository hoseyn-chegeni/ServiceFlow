from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from .models import Note, NoteTag
from django_filters.views import FilterView
from .filters import NoteFilter, PublicNoteFilter, TagFilter
from .forms import CreatePublicNoteForm, CreateNoteForm, CreateTagForm

# Create your views here.


class PublicNoteView(FilterView):
    template_name = "notes/public_notes.html"
    model = Note
    context_object_name = "notes"
    filterset_class = PublicNoteFilter

    def get_queryset(self, **kwargs):
        qs = super().get_queryset(**kwargs)
        return qs.filter(is_public=True, is_archive=False)


class MyNotesView(FilterView):
    template_name = "notes/my_notes.html"
    model = Note
    filterset_class = NoteFilter
    context_object_name = "notes"

    def get_queryset(self, **kwargs):
        qs = super().get_queryset(**kwargs)
        return qs.filter(author_id=self.request.user.id, is_archive=False)


class MyArchiveNotesView(FilterView):
    template_name = "notes/my_archive_notes.html"
    model = Note
    context_object_name = "notes"
    filterset_class = NoteFilter

    def get_queryset(self, **kwargs):
        qs = super().get_queryset(**kwargs)
        return qs.filter(author_id=self.request.user.id, is_archive=True)


class CreateNote(CreateView):
    template_name = "notes/create_note.html"
    form_class = CreateNoteForm
    success_url = reverse_lazy("notes:my_notes")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class CreatePublicNote(CreateView):
    template_name = "notes/create_public_note.html"
    form_class = CreatePublicNoteForm
    success_url = reverse_lazy("notes:public_notes")

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.is_public = True
        return super().form_valid(form)


class NoteDetailView(DetailView):
    model = Note
    template_name = "notes/detail.html"


class NoteUpdateView(UpdateView):
    model = Note
    template_name = "notes/update.html"
    success_url = reverse_lazy("notes:my_notes")
    fields = ("title", "content", "is_archive", "is_public", "tags")


class NoteDeleteView(DeleteView):
    model = Note
    template_name = "notes/update.html"
    success_url = reverse_lazy("notes:my_notes")


class ListTagView(FilterView):
    model = NoteTag
    template_name = "notes/tags/list.html"
    filterset_class = TagFilter
    context_object_name = "tags"

    def get_queryset(self, **kwargs):
        qs = super().get_queryset(**kwargs)
        return qs.filter(is_active=True)


class DisableTagView(FilterView):
    model = NoteTag
    template_name = "notes/tags/disable.html"
    filterset_class = TagFilter
    context_object_name = "tags"

    def get_queryset(self, **kwargs):
        qs = super().get_queryset(**kwargs)
        return qs.filter(is_active=False)


class DetailTagView(DetailView):
    model = NoteTag
    template_name = "notes/tags/detail.html"


class CreateTagView(CreateView):
    model = NoteTag
    template_name = "notes/tags/create.html"
    form_class = CreateTagForm
    success_url = reverse_lazy("notes:list_tag")

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class UpdateTagView(UpdateView):
    model = NoteTag
    template_name = "notes/tags/update.html"
    fields = [
        "name",
        "desc",
        "is_active",
    ]
    success_url = reverse_lazy("notes:list_tag")


class DeleteTagView(DeleteView):
    model = NoteTag
    template_name = "notes/tags/delete.html"
    success_url = reverse_lazy("notes:list_tag")
