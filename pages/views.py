from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import PostViaje


def home(request):
    """Vista de inicio/home."""
    return render(request, "pages/home.html")


def about(request):
    """Vista de 'Acerca de mí'."""
    return render(request, "pages/about.html")


class PostViajeListView(ListView):
    """Listado de posts de viaje."""
    model = PostViaje
    template_name = "pages/pages_list.html"
    context_object_name = "posts"
    paginate_by = 6  

    def get_queryset(self):
        queryset = PostViaje.objects.all().order_by("-fecha_publicacion")
        busqueda = self.request.GET.get("q")
        if busqueda:
            queryset = queryset.filter(titulo__icontains=busqueda)
        return queryset


class PostViajeDetailView(DetailView):
    """Detalle de un post de viaje."""
    model = PostViaje
    template_name = "pages/page_detail.html"
    context_object_name = "post"


@method_decorator(login_required, name="dispatch")
class PostViajeCreateView(CreateView):
    """Crear un nuevo post de viaje (requiere login)."""
    model = PostViaje
    fields = ["titulo", "destino", "contenido", "imagen"]
    template_name = "pages/page_form.html"
    success_url = reverse_lazy("pages_list")

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)


class PostViajeUpdateView(LoginRequiredMixin, UpdateView):
    """Editar un post de viaje existente (requiere login)."""
    model = PostViaje
    fields = ["titulo", "destino", "contenido", "imagen"]
    template_name = "pages/page_form.html"
    success_url = reverse_lazy("pages_list")
    login_url = "/accounts/login/"  


class PostViajeDeleteView(LoginRequiredMixin, DeleteView):
    """Borrar un post de viaje (requiere login)."""
    model = PostViaje
    template_name = "pages/page_confirm_delete.html"
    success_url = reverse_lazy("pages_list")
    login_url = "/accounts/login/"
