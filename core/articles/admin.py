from django.contrib import admin
from .models import Article, ShareArticle,CommentShareArticle

# Register your models here.
admin.site.register(Article)
admin.site.register(ShareArticle)
admin.site.register(CommentShareArticle)
