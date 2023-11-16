from django import forms
from .models import Article, ArticleTags, PendingArticle


class CreateArticleForms(forms.ModelForm):
    class Meta:
        model = PendingArticle
        fields = (
            "title",
            "content",
            "tags",
            "related_articles",
            "is_active",
            "attachments",
        )


class CreateArticleTags(forms.ModelForm):
    class Meta:
        model = ArticleTags
        fields = ("name",)
