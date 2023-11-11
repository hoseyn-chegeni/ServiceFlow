from django.dispatch import receiver
from django.db.models.signals import post_save, pre_delete
from django.core.mail import send_mail
from django.conf import settings
from .models import User
from db_events.models import DatabaseLog


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



@receiver(post_save, sender=User)
def log_user_creation(sender, instance, created, **kwargs):
    if created:
        DatabaseLog.objects.create(
            user=User.objects.get(id = kwargs.get('user').id),
            event_type='create',
            table_name='auth_user',
            record_id=instance.id,
            field_name='All fields',  # Add the specific field name if available
            additional_info='User created',
        )

# Signal to log user update
@receiver(post_save, sender=User)
def log_user_update(sender, instance, created, **kwargs):
    if not created:
        DatabaseLog.objects.create(
            user=User.objects.get(),
            event_type='update',
            table_name='auth_user',
            record_id=instance.id,
            field_name='All fields',  # Add the specific field name if available
            additional_info='User updated',
        )

# Signal to log user deletion
@receiver(pre_delete, sender=User)
def log_user_deletion(sender, instance, **kwargs):
    DatabaseLog.objects.create(
        user=User.objects.get(id = kwargs.get('request.user').id),
        event_type='delete',
        table_name='auth_user',
        record_id=instance.id,
        field_name='All fields',  # Add the specific field name if available
        additional_info='User deleted',
    )