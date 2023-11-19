from django.contrib import admin
from .models import DatabaseLog, TaskLog, UserAuthenticationLog
# Register your models here.
admin.site.register(DatabaseLog)
admin.site.register(TaskLog)
admin.site.register(UserAuthenticationLog)