from django.contrib import admin
from .models import Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ["subject", "from_user", "to_user", "created_at", "is_read"]
    list_filter = ["is_read", "created_at"]
    search_fields = ["subject", "body", "from_user__username", "to_user__username"]
