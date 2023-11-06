from django.db import models


# Create your models here.
def generate_pk():
    if Article.objects.last() is not None:
        number = (Article.objects.last().id) + 1
        return f"ART-{number}"
    else:
        return f"ART-1"


class Article(models.Model):
    art = models.CharField(
        default=generate_pk, max_length=255, unique=True, editable=False
    )
    title = models.CharField(max_length=255)
    content = models.TextField()
    tags = models.ManyToManyField("ArticleTags", blank=True)
    author = models.ForeignKey("accounts.User", on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    related_articles = models.ManyToManyField("self", blank=True)
    is_active = models.BooleanField(default=True)
    approval_status = models.ForeignKey(
        "ArticleApprovalStatus", on_delete=models.SET_NULL, blank=True, null=True
    )
    importance = models.CharField(
        max_length=20,
        choices=[("HIGH", "HIGH"), ("MEDIUM", "MEDIUM"), ("LOW", "LOW")],
        default="MEDIUM",
    )
    attachments = models.FileField(upload_to="attachments", blank=True, null=True)

    def __str__(self):
        return self.title


class ArticleTags(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(
        "accounts.User", on_delete=models.SET_NULL, blank=True, null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class ArticleApprovalStatus(models.Model):
    name = models.CharField(
        max_length=255,
    )
    description = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(
        "accounts.User", on_delete=models.SET_NULL, blank=True, null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ShareArticle(models.Model):
    article = models.ForeignKey('Article', on_delete=models.CASCADE)
    sender = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name= 'sender')
    recipient = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)

    def __str__(self):
        return f'{self.article}'


class CommentShareArticle(models.Model):
    share_article = models.ForeignKey(ShareArticle, on_delete=models.CASCADE)
    content = models.TextField()
    sender = models.ForeignKey('accounts.User', on_delete=models.CASCADE,)
    created_at = models.DateTimeField(auto_now_add= True)


    def __str__(self):
        return f'{self.id}:{self.share_article} '