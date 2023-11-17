from typing import Any
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView,
    UpdateView,
    CreateView,
    DeleteView,
    DetailView,
)
from django_filters.views import FilterView
from .models import (
    Article,
    PendingArticle,
    ArticleTags,
    ShareArticle,
    CommentShareArticle,
    ArticleApprovalStatus,
)
from .forms import CreateArticleForms, CreateArticleTags
from .filters import ArticleFilter, ArticleTagFilter

# Create your views here.


class ListArticleView(LoginRequiredMixin, FilterView):
    model = Article
    context_object_name = "article"
    template_name = "article/list.html"
    filterset_class = ArticleFilter


class MyArticleView(LoginRequiredMixin, FilterView):
    model = Article
    context_object_name = "article"
    template_name = "article/my_list.html"
    filterset_class = ArticleFilter

    def get_queryset(self, **kwargs):
        qs = super().get_queryset(**kwargs)
        return qs.filter(
            approval_status=ArticleApprovalStatus.objects.get(name="Approved"),
            author_id=self.request.user.id,
        )


class ArchiveArticleView(LoginRequiredMixin, FilterView):
    model = Article
    context_object_name = "article"
    template_name = "article/archive.html"
    filterset_class = ArticleFilter

    def get_queryset(self, **kwargs):
        qs = super().get_queryset(**kwargs)
        return qs.filter(is_active=False, author_id=self.request.user.id)


class CreateArticleView(LoginRequiredMixin, CreateView):
    template_name = "article/create.html"
    form_class = CreateArticleForms
    success_url = reverse_lazy("article:list")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class UpdateArticleView(LoginRequiredMixin, UpdateView):
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


class DetailArticleView(LoginRequiredMixin, DetailView):
    model = Article
    template_name = "article/detail.html"


class DeleteArticleView(LoginRequiredMixin, DeleteView):
    model = Article
    template_name = "article/delete.html"
    success_url = reverse_lazy("article:list")


# TAGS
class ListArticleTag(LoginRequiredMixin, FilterView):
    model = ArticleTags
    template_name = "article/tags/list.html"
    context_object_name = "tags"
    filterset_class = ArticleTagFilter


class CreateArticleTag(LoginRequiredMixin, CreateView):
    template_name = "article/tags/create.html"
    form_class = CreateArticleTags
    success_url = reverse_lazy("article:tag_list")


class UpdateArticleTag(LoginRequiredMixin, UpdateView):
    model = ArticleTags
    template_name = "article/tags/update.html"
    fields = ("name",)
    success_url = reverse_lazy("article:tag_list")


class DeleteArticleTag(LoginRequiredMixin, DeleteView):
    model = ArticleTags
    template_name = "article/tags/delete.html"
    success_url = reverse_lazy("article:tag_list")


# SHARED


class ShareArticleDetailView(LoginRequiredMixin, DetailView):
    template_name = "article/shared/detail.html"
    model = ShareArticle

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context["comment"] = self.object.comment.all()
        return context


class SentArticleListView(LoginRequiredMixin, ListView):
    model = ShareArticle
    context_object_name = "article"
    template_name = "article/shared/sent.html"

    def get_queryset(self, **kwargs):
        qs = super().get_queryset(**kwargs)
        return qs.filter(sender_id=self.request.user.id)


class SentArticleView(LoginRequiredMixin, CreateView):
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


class AddCommentView(LoginRequiredMixin, CreateView):
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


class PendingArticleList(LoginRequiredMixin, FilterView):
    model = PendingArticle
    template_name = "article/pending_list.html"
    context_object_name = "tags"
    filterset_class = ArticleFilter

    def get_queryset(self, **kwargs):
        qs = super().get_queryset(**kwargs)
        return qs.filter(
            approval_status=ArticleApprovalStatus.objects.get(name="Pending")
        )


class RejectArticleList(LoginRequiredMixin, FilterView):
    model = PendingArticle
    template_name = "article/reject_list.html"
    context_object_name = "tags"
    filterset_class = ArticleFilter

    def get_queryset(self, **kwargs):
        qs = super().get_queryset(**kwargs)
        return qs.filter(
            approval_status=ArticleApprovalStatus.objects.get(name="Rejected")
        )


class ApproveArticleView(LoginRequiredMixin, UpdateView):
    model = PendingArticle
    template_name = "article/approve.html"
    fields = ("approve_comment",)
    success_url = reverse_lazy("article:pending_list")

    def form_valid(self, form):
        article = form.save(commit=False)
        article.save()
        form.instance.approval_status = ArticleApprovalStatus.objects.get(
            name="Approved"
        )
        Article.objects.create(
            title=article.title,
            content=article.content,
            author=article.author,
            approve_comment=article.approve_comment,
        )
        return super().form_valid(form)


class RejectArticleView(LoginRequiredMixin, UpdateView):
    model = PendingArticle
    template_name = "article/reject.html"
    fields = ("approve_comment",)
    success_url = reverse_lazy("article:pending_list")

    def form_valid(self, form):
        form.instance.approval_status = ArticleApprovalStatus.objects.get(
            name="Rejected"
        )
        return super().form_valid(form)
