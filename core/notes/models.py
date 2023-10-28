from django.db import models
from accounts.models import User
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


# Create your models here.
def generate_pk():
    number = (Note.objects.all().count()) + 1
    return f"NOTE-{number}"


class Note(models.Model):
    note = models.CharField(
        default=generate_pk,
        max_length=255,
        unique=True,
        editable=False,
        verbose_name="Note ID",
    )
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_archive = models.BooleanField(default=False)
    is_public = models.BooleanField(default=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField("NoteTag")

    def __str__(self):
        return self.note


class NoteTag(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
