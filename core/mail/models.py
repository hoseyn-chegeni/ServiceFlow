from django.db import models


# Create your models here.
class Mail(models.Model):
    sender = models.EmailField()
    recipient = models.EmailField()
    subject = models.CharField(
        max_length=255,
    )
    body = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    is_archived = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    is_starred = models.BooleanField(default=False)
    cc = models.EmailField(blank=True, null=True)
    bcc = models.EmailField(blank=True, null=True)
    attachments = models.FileField(upload_to="attachments", blank=True, null=True)
    importance = models.CharField(
        max_length=20, choices=[("HIGH", "HIGH"), ("MEDIUM", "MEDIUM"), ("LOW", "LOW")]
    )
    folder = models.CharField(
        max_length=20,
        choices=[("INBOX", "INBOX"), ("SENT", "SENT"), ("DRAFT", "DRAFT")],
    )
    is_draft = models.BooleanField(default=False)
    reply_to = models.EmailField(blank=True, null=True)
    thread_it = models.CharField(max_length=255, blank=True, null=True)
    is_replied = models.BooleanField(default=False)
    tags = models.ManyToManyField("Tag", blank=True)
    is_forwarded = models.BooleanField(default=False)

    def __str__(self):
        return self.subject


class Tag(models.Model):
    name = models.CharField(max_length=255)
