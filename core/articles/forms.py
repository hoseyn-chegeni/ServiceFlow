from django import forms
from .models import Article, ArticleTags


class CreateArticleForms(forms.ModelForm):
    class Meta:
        model = Article
        fields = ("title", "content", "tags", "related_articles", "is_active")


class CreateArticleTags(forms.ModelForm):
    class Meta:
        model = ArticleTags
        fields = ("name",)
