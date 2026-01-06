from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import PostViajeForm, CategoriaForm, DestinoForm
from .models import PostViaje, Categoria, Destino, Comentario


def home(request):
    ultimos = PostViaje.objects.select_related("autor", "categoria", "destino").order_by("-fecha", "-creado_el")[:6]
    return render(request, "pages/home.html", {"ultimos": ultimos})


@login_required
def about(request):
    return render(request, "pages/about.html")


class PostViajeListView(ListView):
    model = PostViaje
    template_name = "pages/pages_list.html"
    context_object_name = "posts"
    paginate_by = 9

    def get_queryset(self):
        qs = (
            PostViaje.objects.select_related("autor", "categoria", "destino")
            .all()
            .order_by("-fecha", "-creado_el")
        )
        q = self.request.GET.get("q")
        if q:
            qs = qs.filter(titulo__icontains=q)
        return qs


class PostViajeDetailView(DetailView):
    model = PostViaje
    template_name = "pages/pages_detail.html"
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["comentarios"] = Comentario.objects.select_related("autor").filter(post=self.object)
        return ctx


class PostViajeCreateView(LoginRequiredMixin, CreateView):
    model = PostViaje
    form_class = PostViajeForm
    template_name = "pages/page_form.html"
    success_url = reverse_lazy("pages_list")

    def form_valid(self, form):
        form.instance.autor = self.request.user
        messages.success(self.request, "Viaje publicado correctamente.")
        return super().form_valid(form)


class EsAutorMixin(UserPassesTestMixin):
    def test_func(self):
        obj = self.get_object()
        return obj.autor == self.request.user

    def handle_no_permission(self):
        messages.error(self.request, "No tenés permiso para realizar esta acción.")
        return super().handle_no_permission()


class PostViajeUpdateView(LoginRequiredMixin, EsAutorMixin, UpdateView):
    model = PostViaje
    form_class = PostViajeForm
    template_name = "pages/page_form.html"

    def get_success_url(self):
        messages.success(self.request, "Viaje actualizado.")
        return reverse_lazy("page_detail", kwargs={"pk": self.object.pk})


class PostViajeDeleteView(LoginRequiredMixin, EsAutorMixin, DeleteView):
    model = PostViaje
    template_name = "pages/page_confirm_delete.html"
    success_url = reverse_lazy("pages_list")

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Viaje eliminado.")
        return super().delete(request, *args, **kwargs)


class CategoriaCreateView(LoginRequiredMixin, CreateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = "pages/categoria_form.html"
    success_url = reverse_lazy("pages_list")

    def form_valid(self, form):
        messages.success(self.request, "Categoría creada.")
        return super().form_valid(form)


class DestinoCreateView(LoginRequiredMixin, CreateView):
    model = Destino
    form_class = DestinoForm
    template_name = "pages/destino_form.html"
    success_url = reverse_lazy("pages_list")

    def form_valid(self, form):
        messages.success(self.request, "Destino creado.")
        return super().form_valid(form)


@login_required
def comentario_create(request, pk):
    post = get_object_or_404(PostViaje, pk=pk)
    if request.method == "POST":
        texto = (request.POST.get("texto") or "").strip()
        if texto:
            Comentario.objects.create(post=post, autor=request.user, texto=texto)
            messages.success(request, "Comentario publicado.")
        else:
            messages.error(request, "El comentario no puede estar vacío.")
    return redirect("page_detail", pk=post.pk)
