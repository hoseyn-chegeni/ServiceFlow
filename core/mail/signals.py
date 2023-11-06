from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.mail import send_mail
from django.conf import settings
from .models import Mail


@receiver(post_save, sender=Mail)
def send_to_smtp(sender, instance, created, **kwargs):
    if created:
        subject = instance.subject
        message = instance.body
        from_email = instance.sender
        recipient_list = [
            instance.recipient,
        ]

        send_mail(subject, message, from_email, recipient_list)
