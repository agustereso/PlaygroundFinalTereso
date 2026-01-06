from django.urls import path
from .views import InboxView, SentView, MessageDetailView, MessageCreateView

app_name = "messaging"

urlpatterns = [
    path("messages/", InboxView.as_view(), name="inbox"),
    path("messages/sent/", SentView.as_view(), name="sent"),
    path("messages/new/", MessageCreateView.as_view(), name="message_create"),
    path("messages/<int:pk>/", MessageDetailView.as_view(), name="message_detail"),
]
