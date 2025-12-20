from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Message
from .forms import MessageForm


@login_required
def inbox_view(request):
    mensajes = Message.objects.filter(recipient=request.user)
    return render(request, "messaging/inbox.html", {"mensajes": mensajes})


@login_required
def sent_view(request):
    mensajes = Message.objects.filter(sender=request.user)
    return render(request, "messaging/sent.html", {"mensajes": mensajes})


@login_required
def message_detail_view(request, pk):
    mensaje = get_object_or_404(Message, pk=pk)
    if mensaje.recipient == request.user and not mensaje.is_read:
        mensaje.is_read = True
        mensaje.save()
    return render(request, "messaging/message_detail.html", {"mensaje": mensaje})


@login_required
def message_create_view(request):
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            mensaje = form.save(commit=False)
            mensaje.sender = request.user
            mensaje.save()
            messages.success(request, "Mensaje enviado correctamente.")
            return redirect("inbox")
    else:
        form = MessageForm()
    return render(request, "messaging/message_form.html", {"form": form})
