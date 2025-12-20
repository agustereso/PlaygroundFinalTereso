from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class PostViaje(models.Model):
    objects = models.Manager()

    titulo = models.CharField(max_length=200)
    destino = models.CharField(max_length=100)
    contenido = RichTextField()
    imagen = models.ImageField(upload_to="posts_viajes/", blank=True, null=True)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts_viajes")

    class Meta:
        ordering = ["-fecha_publicacion"]

    def __str__(self):
        return f"{self.titulo} - {self.destino}"
