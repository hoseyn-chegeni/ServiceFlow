from django.db import models
from accounts.models import User
from django.dispatch import receiver


# Create your models here.
def generate_pk():
    pass


class Note(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_archive = models.BooleanField(default=False)
    is_public = models.BooleanField(default=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField("NoteTag", blank=True)
    attachment = models.FileField(upload_to="attachments", blank=True, null=True)

    def __str__(self):
        return self.note


class NoteTag(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_by = models.ForeignKey(
        "accounts.User", blank=True, null=True, on_delete=models.SET_NULL
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
