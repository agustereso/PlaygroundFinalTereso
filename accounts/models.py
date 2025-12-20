from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    
    objects = models.Manager()
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    avatar = models.ImageField(upload_to="avatars/", blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    link = models.URLField(blank=True, null=True)


def __str__(self):
    return f"Perfil de {self.user}"
