from django.urls import path
from . import views

urlpatterns = [
    path("inbox/", views.inbox_view, name="inbox"),
    path("sent/", views.sent_view, name="sent"),
    path("new/", views.message_create_view, name="message_new"),
    path("<int:pk>/", views.message_detail_view, name="message_detail"),
]
