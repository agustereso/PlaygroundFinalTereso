from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView

from .forms import MessageForm
from .models import Message


class InboxView(LoginRequiredMixin, ListView):
    model = Message
    template_name = "messaging/inbox.html"
    context_object_name = "mensajes"
    paginate_by = 10

    def get_queryset(self):
        qs = Message.objects.select_related("from_user", "to_user").filter(to_user=self.request.user)
        q = self.request.GET.get("q")
        if q:
            qs = qs.filter(Q(subject__icontains=q) | Q(body__icontains=q) | Q(from_user__username__icontains=q))
        return qs


class SentView(LoginRequiredMixin, ListView):
    model = Message
    template_name = "messaging/sent.html"
    context_object_name = "mensajes"
    paginate_by = 10

    def get_queryset(self):
        qs = Message.objects.select_related("from_user", "to_user").filter(from_user=self.request.user)
        q = self.request.GET.get("q")
        if q:
            qs = qs.filter(Q(subject__icontains=q) | Q(body__icontains=q) | Q(to_user__username__icontains=q))
        return qs


class MessageDetailView(LoginRequiredMixin, DetailView):
    model = Message
    template_name = "messaging/message_detail.html"
    context_object_name = "mensaje"

    def get_object(self, queryset=None):
        obj = get_object_or_404(
            Message.objects.select_related("from_user", "to_user"),
            pk=self.kwargs["pk"],
        )
        user = self.request.user
        if obj.to_user != user and obj.from_user != user:
            raise PermissionError("No autorizado")
        if obj.to_user == user and not obj.is_read:
            obj.is_read = True
            obj.save(update_fields=["is_read"])
        return obj


class MessageCreateView(LoginRequiredMixin, CreateView):
    model = Message
    form_class = MessageForm
    template_name = "messaging/message_form.html"
    
    def get_success_url(self):
        return reverse("messaging:inbox")
    
    def form_valid(self, form):
        form.instance.from_user = self.request.user
        messages.success(self.request, "Mensaje enviado.")
        return super().form_valid(form)
