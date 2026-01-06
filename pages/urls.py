from django.urls import path
from .views import (
    home,
    about,
    PostViajeListView,
    PostViajeDetailView,
    PostViajeCreateView,
    PostViajeUpdateView,
    PostViajeDeleteView,
    CategoriaCreateView,
    DestinoCreateView,
    comentario_create,
)

urlpatterns = [
    path("", home, name="home"),
    path("about/", about, name="about"),
    path("pages/", PostViajeListView.as_view(), name="pages_list"),
    path("pages/<int:pk>/", PostViajeDetailView.as_view(), name="page_detail"),
    path("pages/crear/", PostViajeCreateView.as_view(), name="page_create"),
    path("pages/<int:pk>/editar/", PostViajeUpdateView.as_view(), name="page_update"),
    path("pages/<int:pk>/borrar/", PostViajeDeleteView.as_view(), name="page_delete"),
    path("categorias/crear/", CategoriaCreateView.as_view(), name="categoria_create"),
    path("destinos/crear/", DestinoCreateView.as_view(), name="destino_create"),
    path("pages/<int:pk>/comentar/", comentario_create, name="comentario_create"),
]
