from django import forms
from   .models import Note




class CreateNoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ("title","content","tags","is_public")


class CreatePublicNoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ("title","content","tags",)