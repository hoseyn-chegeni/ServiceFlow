from django.urls import path
from .views import PublicNoteView,MyNotesView, MyArchiveNotesView,CreatePublicNote,CreateNote

app_name = 'notes'

urlpatterns = [
    path('public_notes/',PublicNoteView.as_view(), name='public_notes'),
    path('my_notes/',MyNotesView.as_view(), name='my_notes'),
    path('my_archive_notes/',MyArchiveNotesView.as_view(), name='my_archive_notes'),
    path('create_public_note/',CreatePublicNote.as_view(), name='create_public_note'),
    path('create_note/',CreateNote.as_view(), name='create_note'),

]