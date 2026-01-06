from django import forms
from django.contrib.auth import get_user_model
from .models import Message

User = get_user_model()


class MessageForm(forms.ModelForm):
    to_user = forms.ModelChoiceField(
        queryset=User.objects.all().order_by("username"),
        widget=forms.Select(attrs={"class": "form-select"}),
        label="Para",
    )

    class Meta:
        model = Message
        fields = ["to_user", "subject", "body"]
        widgets = {
            "subject": forms.TextInput(attrs={"class": "form-control", "placeholder": "Asunto"}),
            "body": forms.Textarea(attrs={"class": "form-control", "rows": 6, "placeholder": "Escribí tu mensaje..."}),
        }
