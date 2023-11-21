from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import UserRole


@receiver(post_save, sender=UserRole)
def update_user_permissions(sender, instance, created, **kwargs):
    if created:
        user = instance.user
        role = instance.role
        permissions = role.permissions.all()  # Get permissions associated with the role
        user.user_permissions.add(*permissions)


@receiver(post_delete, sender=UserRole)
def remove_user_permissions(sender, instance, **kwargs):
    user = instance.user
    role = instance.role
    permissions = role.permissions.all()  # Get permissions associated with the role
    user.user_permissions.remove(*permissions)
