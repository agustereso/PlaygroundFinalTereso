from django import forms
from .models import PostViaje, Categoria, Destino


class PostViajeForm(forms.ModelForm):
    class Meta:
        model = PostViaje
        fields = ["titulo", "categoria", "destino", "contenido", "imagen"]
        widgets = {
            "titulo": forms.TextInput(attrs={"class": "form-control", "placeholder": "Título"}),
            "categoria": forms.Select(attrs={"class": "form-select"}),
            "destino": forms.Select(attrs={"class": "form-select"}),
        }


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ["nombre"]
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control", "placeholder": "Ej: Aventura"}),
        }


class DestinoForm(forms.ModelForm):
    class Meta:
        model = Destino
        fields = ["nombre", "pais"]
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control", "placeholder": "Ej: Bariloche"}),
            "pais": forms.TextInput(attrs={"class": "form-control", "placeholder": "Ej: Argentina"}),
        }
