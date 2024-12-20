from django.db.models.signals import post_save
from django.dispatch import receiver
from core.models import CustomUserModel
from .models import Cart


@receiver(post_save, sender=CustomUserModel)
def create_user_cart(sender, instance, created, **kwargs):
    if created:
        Cart.objects.create(user=instance)
