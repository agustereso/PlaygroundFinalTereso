from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.db.utils import OperationalError, ProgrammingError

from .models import Profile

User = get_user_model()


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if not created:
        return
    try:
        Profile.objects.create(user=instance)
    except (OperationalError, ProgrammingError):
        return
