from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import PostViajeForm
from .models import PostViaje


def home(request):
    ultimos = PostViaje.objects.order_by("-fecha")[:6]
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
        qs = super().get_queryset().order_by("-fecha")
        q = self.request.GET.get("q")
        if q:
            qs = qs.filter(titulo__icontains=q)
        return qs


class PostViajeDetailView(DetailView):
    model = PostViaje
    template_name = "pages/page_detail.html"
    context_object_name = "post"


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
