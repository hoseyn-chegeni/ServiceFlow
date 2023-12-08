from django.db import models
from accounts.models import User

# Create your models here.


def generate_pk():
    pass


class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    creator = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="reaporter"
    )
    type = models.ForeignKey(
        "TaskType", on_delete=models.SET_NULL, blank=True, null=True
    )
    created_date = models.DateTimeField(auto_now_add=True)
    last_change = models.DateTimeField(auto_now=True)
    status = models.ForeignKey(
        "TaskStatus", on_delete=models.SET_NULL, blank=True, null=True
    )
    assign_to = models.ForeignKey(
        User, on_delete=models.SET_NULL, blank=True, null=True, related_name="Assigner"
    )
    priority = models.ForeignKey(
        "TaskPriority", on_delete=models.SET_NULL, blank=True, null=True
    )
    participants = models.ManyToManyField(
        User, related_name="tasks_participated", blank=True
    )

    def __str__(self):
        return self.title


class TaskType(models.Model):
    name = models.CharField(max_length=255)
    assigned_to = models.ForeignKey(
        "team.Team", on_delete=models.SET_NULL, blank=True, null=True
    )
    description = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(
        "accounts.User", on_delete=models.SET_NULL, blank=True, null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class TaskStatus(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(
        "accounts.User", on_delete=models.SET_NULL, blank=True, null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class TaskPriority(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    badge = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.ForeignKey(
        "accounts.User", on_delete=models.SET_NULL, blank=True, null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class TaskComment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    commented_at = models.DateTimeField(auto_now_add=True)
    attachment_title = models.CharField(
        max_length=50, default="attachment", blank=True, null=True
    )
    attachments = models.FileField(upload_to="attachments", blank=True, null=True)

    def __str__(self):
        return f"{self.task.title}/ {self.user.email}"
