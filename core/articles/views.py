from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    UpdateView,
    CreateView,
    DeleteView,
    DetailView,
)
from django_filters.views import FilterView
from .models import Article, ArticleTags
from .forms import CreateArticleForms, CreateArticleTags
from .filters import ArticleFilter, ArticleTagFilter

# Create your views here.


class ListArticleView(FilterView):
    model = Article
    context_object_name = "article"
    template_name = "article/list.html"
    filterset_class = ArticleFilter


class MyArticleView(FilterView):
    model = Article
    context_object_name = "article"
    template_name = "article/my_list.html"
    filterset_class = ArticleFilter

    def get_queryset(self, **kwargs):
        qs = super().get_queryset(**kwargs)
        return qs.filter(is_active=True, author_id=self.request.user.id)


class ArchiveArticleView(FilterView):
    model = Article
    context_object_name = "article"
    template_name = "article/archive.html"
    filterset_class = ArticleFilter

    def get_queryset(self, **kwargs):
        qs = super().get_queryset(**kwargs)
        return qs.filter(is_active=False, author_id=self.request.user.id)


class CreateArticleView(CreateView):
    template_name = "article/create.html"
    form_class = CreateArticleForms
    success_url = reverse_lazy("article:list")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class UpdateArticleView(UpdateView):
    model = Article
    fields = ("title", "content", "tags", "related_articles", "is_active")
    template_name = "article/update.html"
    success_url = reverse_lazy("article:my_list")


class DetailArticleView(DetailView):
    model = Article
    template_name = "article/detail.html"


class DeleteArticleView(DeleteView):
    model = Article
    template_name = "article/delete.html"
    success_url = reverse_lazy("article:list")


# TAGS
class ListArticleTag(FilterView):
    model = ArticleTags
    template_name = "article/tags/list.html"
    context_object_name = "tags"
    filterset_class = ArticleTagFilter


class CreateArticleTag(CreateView):
    template_name = "article/tags/create.html"
    form_class = CreateArticleTags
    success_url = reverse_lazy("article:tag_list")


class UpdateArticleTag(UpdateView):
    model = ArticleTags
    template_name = "article/tags/update.html"
    fields = ("name",)
    success_url = reverse_lazy("article:tag_list")


class DeleteArticleTag(DeleteView):
    model = ArticleTags
    template_name = "article/tags/delete.html"
    success_url = reverse_lazy("article:tag_list")
