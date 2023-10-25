from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.mail import send_mail
from django.conf import settings
from .models import Task

@receiver(post_save, sender = Task)
def send_mail_compelete_task(sender, instance, **kwargs):
        subject = f'Dear {instance.assign_to} A new task with title ({instance.title}) Assigned to you '
        message = f'{instance.task}/// {instance.title}///{instance.creator}/// {instance.description}'
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [instance.assign_to.email]
        send_mail(subject, message, from_email, recipient_list)

