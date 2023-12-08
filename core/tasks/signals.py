from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Task


@receiver(post_save, sender=Task)
def add_creator_as_participant(sender, instance, created, **kwargs):
    if created:
        # 'instance' represents the newly created Task
        instance.participants.add(instance.created_by)
        instance.participants.add(instance.assign_to)
