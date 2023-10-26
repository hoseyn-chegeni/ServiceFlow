from django import forms
from   .models import Note


class CreatePublicNoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ("title","content","tags",)