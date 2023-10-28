from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.mail import send_mail
from django.conf import settings
from .models import Reminder


@receiver(post_save, sender=Reminder)
def send_mail_assigned_reminder(sender, instance, created, **kwargs):
    if created:
        subject = f"new reminder "
        message = f" new reminder assign to you"
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [user for user in instance.assign_to.all()]

        send_mail(subject, message, from_email, recipient_list)


post_save.connect(send_mail_assigned_reminder, sender=Reminder)
