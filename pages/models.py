from django.conf import settings
from django.db import models
from ckeditor.fields import RichTextField


class Categoria(models.Model):
    nombre = models.CharField(max_length=60, unique=True)
    objects = models.Manager()

    def __str__(self):
        return str(self.nombre)


class Destino(models.Model):
    nombre = models.CharField(max_length=80, unique=True)
    pais = models.CharField(max_length=80, blank=True)
    objects = models.Manager()

    def __str__(self):
        if self.pais:
            return f"{self.nombre}, {self.pais}"
        return str(self.nombre)


class PostViaje(models.Model):
    titulo = models.CharField(max_length=200)
    destino = models.ForeignKey(
        Destino, on_delete=models.SET_NULL, null=True, blank=True, related_name="posts"
    )
    categoria = models.ForeignKey(
        Categoria, on_delete=models.SET_NULL, null=True, blank=True, related_name="posts"
    )
    contenido = RichTextField()
    imagen = models.ImageField(upload_to="posts_viajes/", blank=True, null=True)
    fecha = models.DateField(auto_now_add=True)
    creado_el = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="viajes")

    objects = models.Manager()

    class Meta:
        ordering = ["-fecha", "-creado_el"]

    def __str__(self):
        return str(self.titulo)


class Comentario(models.Model):
    post = models.ForeignKey(PostViaje, on_delete=models.CASCADE, related_name="comentarios")
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="comentarios")
    texto = models.TextField(max_length=500)
    creado_el = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()

    class Meta:
        ordering = ["-creado_el"]

    def __str__(self):
        # pylint: disable=no-member,unsubscriptable-object
        return f"{self.autor.username}: {self.texto[:30]}"
