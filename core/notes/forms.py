from django import forms
from .models import Note, NoteTag


class CreateNoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ("title", "content", "tags", "is_public", "attachment")


class CreatePublicNoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ("title", "content", "tags", "attachment")


class CreateTagForm(forms.ModelForm):
    class Meta:
        model = NoteTag
        fields = (
            "name",
            "desc",
        )
