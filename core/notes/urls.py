from django.urls import path
from .views import PublicNoteView,MyNotesView

app_name = 'notes'

urlpatterns = [
    path('public_notes/',PublicNoteView.as_view(), name='public_notes'),
    path('my_note/',MyNotesView.as_view(), name='my_notes'),
]