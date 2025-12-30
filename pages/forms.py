from django import forms
from .models import PostViaje

class PostViajeForm(forms.ModelForm):
    class Meta:
        model = PostViaje
        fields = "__all__"
        labels = {
            "titulo": "Título",
            "destino": "Destino",
            "contenido": "Contenido",
            "imagen": "Imagen",
            "fecha": "Fecha",
        }
        error_messages = {
            "titulo": {"required": "El título es obligatorio."},
            "destino": {"required": "El destino es obligatorio."},
            "contenido": {"required": "El contenido es obligatorio."},
            "fecha": {"required": "La fecha es obligatoria.", "invalid": "Ingresá una fecha válida."},
            "imagen": {"invalid": "Subí una imagen válida."},
        }

        widgets = {
            "titulo": forms.TextInput(attrs={"placeholder": "Ej: Aventura en Bariloche"}),
            "destino": forms.TextInput(attrs={"placeholder": "Ej: Bariloche, Argentina"}),
            "fecha": forms.DateInput(attrs={"type": "date"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            if isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs.update({"class": "form-check-input"})
            elif isinstance(field.widget, forms.ClearableFileInput):
                field.widget.attrs.update({"class": "form-control"})
            else:
                field.widget.attrs.update({"class": "form-control"})
