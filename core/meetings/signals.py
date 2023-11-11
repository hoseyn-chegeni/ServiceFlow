from django.dispatch import receiver
from django.db.models.signals import post_save, m2m_changed
from django.core.mail import send_mail
from django.conf import settings
from .models import Meetings
from accounts.models import User


@receiver(m2m_changed, sender=Meetings.attendees.through)
def send_mail_for_attendees(sender, instance, action, model, pk_set, **kwargs):
    if action == 'post_add':
        subject = f"{instance.organizer} has book a new meeting at {instance.date_time} for you"
        message = f"{instance.title}, {instance.description}"
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [User.objects.get(pk=pk).email for pk in pk_set]
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
