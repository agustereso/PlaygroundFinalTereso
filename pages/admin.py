from django.contrib import admin
from .models import Categoria, Destino, PostViaje, Comentario


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    search_fields = ["nombre"]


@admin.register(Destino)
class DestinoAdmin(admin.ModelAdmin):
    search_fields = ["nombre", "pais"]


@admin.register(PostViaje)
class PostViajeAdmin(admin.ModelAdmin):
    list_display = ["titulo", "autor", "fecha", "creado_el"]
    search_fields = ["titulo", "autor__username"]
    list_filter = ["fecha", "categoria", "destino"]


@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ["post", "autor", "creado_el"]
    search_fields = ["post__titulo", "autor__username", "texto"]
