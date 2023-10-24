from django.urls import path
from .views import PublicNoteView

app_name = 'notes'

urlpatterns = [
    path('public_notes/',PublicNoteView.as_view(), name='public_notes'),
]