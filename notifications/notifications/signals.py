# your_app_name/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from .models import Notification 

@receiver(post_save, sender=User)
def send_notification(sender, instance, created, **kwargs):
    if created:
        print(f"New user created: {instance.username}")  # Add this for debugging
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "notifications",
            {
                "type": "send_notification",
                "message": f"New user created: {instance.username}",
            }
        )

        Notification.objects.create(
            user=instance,
            notification_type='user_creation',
            message=f"New user created: {instance.username}",
            status='sent',
        )
