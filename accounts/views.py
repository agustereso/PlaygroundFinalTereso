from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib import messages

from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm


def signup_view(request):
    """Registro de usuario."""
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Tu cuenta fue creada correctamente.")
            login(request, user)
            return redirect("home")
    else:
        form = UserRegisterForm()
    return render(request, "accounts/signup.html", {"form": form})


def login_view(request):
    """Login de usuario."""
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Has iniciado sesión.")
            return redirect("home")
    else:
        form = AuthenticationForm()
    return render(request, "accounts/login.html", {"form": form})


def logout_view(request):
    """Logout de usuario."""
    logout(request)
    messages.info(request, "Has cerrado sesión.")
    return redirect("home")


@login_required
def profile_view(request):
    """Vista de perfil (decorador en vista común ✅)."""
    return render(request, "accounts/profile.html", {"user": request.user})


@login_required
def profile_edit_view(request):
    """Editar datos de usuario y perfil."""
    if request.method == "POST":
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile
        )
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Tu perfil se actualizó correctamente.")
            return redirect("profile")
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        "user_form": user_form,
        "profile_form": profile_form,
    }
    return render(request, "accounts/profile_edit.html", context)


@login_required
def password_change_view(request):
    """Cambiar contraseña."""
    if request.method == "POST":
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Contraseña actualizada.")
            return redirect("profile")
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, "accounts/password_change.html", {"form": form})
