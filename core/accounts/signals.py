from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.mail import send_mail
from django.conf import settings
from .models import User


@receiver(post_save, sender=User)
def send_mail_create_user(sender, instance, created, **kwargs):
    if created:
        subject = f"Dear {instance.first_name}{instance.last_name} Your account has been created in ITSM "
        message = f"Your accounts with has been created for change password and login to your accounts please click here"
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [instance.email]
        send_mail(subject, message, from_email, recipient_list)


# @receiver(post_save, sender=User)
# def set_user_group(sender, instance, created, **kwargs):
#     if created:
#         user = User.objects.get(id=instance.id)
#         user.groups.add(
#             user.member_of.access_group,
#         )
#         user.save()
