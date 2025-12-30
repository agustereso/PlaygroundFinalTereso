from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField
from datetime import date

class PostViaje(models.Model):
    objects = models.Manager()

    titulo = models.CharField(max_length=200)
    destino = models.CharField(max_length=100)
    contenido = RichTextField()
    imagen = models.ImageField(upload_to="posts_viajes/", blank=True, null=True)

    fecha = models.DateField(default=date.today)
    creado_el = models.DateTimeField(auto_now_add=True)

    autor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="viajes"
    )

    class Meta:
        ordering = ["-fecha", "-creado_el"]

    def __str__(self):
        return f"{self.titulo} - {self.destino}"
