from django.contrib import admin
from .models import (
    Article,
    ShareArticle,
    CommentShareArticle,
    ArticleApprovalStatus,
    PendingArticle,
)

# Register your models here.
admin.site.register(Article)
admin.site.register(ShareArticle)
admin.site.register(CommentShareArticle)
admin.site.register(ArticleApprovalStatus)
admin.site.register(PendingArticle)
