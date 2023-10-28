from django.contrib import admin
from .models import NoteTag, Note

# Register your models here.
admin.site.register(Note)
admin.site.register(NoteTag)
