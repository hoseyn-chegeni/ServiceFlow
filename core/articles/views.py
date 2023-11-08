from typing import Any
from django.db import models
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    UpdateView,
    CreateView,
    DeleteView,
    DetailView,
)
from django_filters.views import FilterView
from .models import Article, ArticleTags, ShareArticle, CommentShareArticle
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
    fields = (
        "title",
        "content",
        "tags",
        "related_articles",
        "is_active",
        "attachments",
    )
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


# SHARED


class ShareArticleDetailView(DetailView):
    template_name = "article/shared/detail.html"
    model = ShareArticle

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context["comment"] = self.object.comment.all()
        return context


class SentArticleListView(ListView):
    model = ShareArticle
    context_object_name = "article"
    template_name = "article/shared/sent.html"

    def get_queryset(self, **kwargs):
        qs = super().get_queryset(**kwargs)
        return qs.filter(sender_id=self.request.user.id)


class SentArticleView(CreateView):
    model = ShareArticle
    fields = (
        "recipient",
        "content",
    )
    success_url = reverse_lazy("article:list")
    template_name = "article/shared/post.html"

    def form_valid(self, form):
        article = get_object_or_404(Article, id=self.kwargs["article_id"])
        form.instance.article = article
        form.instance.sender = self.request.user
        return super().form_valid(form)


class AddCommentView(CreateView):
    model = CommentShareArticle
    fields = ("content",)
    template_name = "article/shared/comment.html"

    def get_success_url(self) -> str:
        return reverse_lazy(
            "article:share_detail", kwargs={"pk": self.kwargs["article_id"]}
        )

    def form_valid(self, form):
        article = get_object_or_404(ShareArticle, id=self.kwargs["article_id"])
        form.instance.share_article = article
        form.instance.sender = self.request.user
        return super().form_valid(form)


# APPROVAL WORK FLOW


class ApproveArticleView:
    pass
