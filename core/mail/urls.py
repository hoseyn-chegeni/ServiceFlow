from django.urls import path
from .views import MailBoxView, SentItemView

app_name = "mail"

urlpatterns = [
    path("inbox/", MailBoxView.as_view(), name="inbox"),
    path("sent/", SentItemView.as_view(), name="sent"),
]
