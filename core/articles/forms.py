from django import forms
from .models import Article


class CreateArticleForms(forms.ModelForm):
    class Meta:
        model = Article
        fields = ("title", "content", "tags", "related_articles", "is_active")
