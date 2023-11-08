from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.mail import send_mail
from django.conf import settings
from .models import Meetings


@receiver(post_save, sender=Meetings)
def send_mail_for_attendees(sender, instance, created, **kwargs):
    if created:
        subject = f"{instance.organizer} has book a new meeting at {instance.date_time} for you"
        message = f"{instance.title}, {instance.description}"
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [i.email for i in instance.attendees.all()]
        send_mail(subject, message, from_email, recipient_list)


@receiver(post_save, sender=Meetings)
def send_mail_for_organizer(sender, instance, created, **kwargs):
    if created:
        subject = f"Dear {instance.organizer} you {instance.title} meeting has set for {instance.date_time}"
        message = f"{instance.title}, {instance.description}"
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [
            instance.organizer,
        ]
        send_mail(subject, message, from_email, recipient_list)
