from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.mail import send_mail
from django.conf import settings
from .models import Reminder
from mail.models import Mail


@receiver(post_save, sender=Reminder)
def send_mail_assigned_reminder(sender, instance, created, **kwargs):
        for i in instance.assign_to.all():
            Mail.objects.create(
                sender = instance.created_by,
                recipient = instance.created_by,
                body = instance.title,
                subject = instance.title,
            )

