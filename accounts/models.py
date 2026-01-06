from django.conf import settings
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="profile")
    avatar = models.ImageField(upload_to="avatars/", blank=True, null=True)
    bio = models.CharField(max_length=240, blank=True)

    objects = models.Manager()

    def __str__(self):
        # pylint: disable=no-member
        return getattr(self.user, "username", str(self.user))
