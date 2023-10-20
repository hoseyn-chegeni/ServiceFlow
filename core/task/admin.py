from django.contrib import admin
from .models import TASK, TaskStatus, TaskType

# Register your models here.
admin.site.register(TASK)
admin.site.register(TaskType)
admin.site.register(TaskStatus)
