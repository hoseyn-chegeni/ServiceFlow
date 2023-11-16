from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.mail import send_mail
from django.conf import settings
from .models import  TaskPriorityChange, TaskAssignmentHistory
from db_events.models import TaskLog


@receiver(post_save, sender=TaskPriorityChange)
def log_task_priority(sender, instance, created, **kwargs):
    if created:
        TaskLog.objects.create(
            user=instance.changed_by,
            task = instance.task,
            event_type="Change Priority",
            additional_info=f"{instance.changed_by} Set '{instance.priority}' for {instance.task}",
        )

@receiver(post_save, sender=TaskAssignmentHistory)
def log_task_assignment(sender, instance, created, **kwargs):
    if created:
        TaskLog.objects.create(
            user=instance.assigned_by,
            task = instance.task,
            event_type="Assignment",
            additional_info=f"{instance.assigned_by} Assigned Task to {instance.assigned_to}",
        )