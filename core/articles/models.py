from django.db import models

# Create your models here.
def generate_pk():
    if Article.objects.last() is not None:
        number = (Article.objects.last().id) + 1
        return f"ART-{number}"
    else:
        return f"ART-1"
    

class Article(models.Model):
    art = models.CharField(default=generate_pk, max_length=255, unique=True, editable=False)
    title = models.CharField(max_length=255)
    content = models.TextField()
    tags = models.ManyToManyField('ArticleTags')
    author = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    related_articles = models.ManyToManyField('self')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class ArticleTags(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    