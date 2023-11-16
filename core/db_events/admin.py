from django.contrib import admin
from .models import DatabaseLog, TaskLog

# Register your models here.
admin.site.register(DatabaseLog)
admin.site.register(TaskLog)
