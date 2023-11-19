from django.contrib import admin
from .models import DatabaseLog, TaskLog, UserAuthenticationLog
# Register your models here.

class UserAuthenticationLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'login_time', 'ip_address', 'status')
    search_fields = ('user__email', 'ip_address')
    list_filter = ('status',)
    readonly_fields = ("login_time",)

admin.site.register(DatabaseLog)
admin.site.register(TaskLog)
admin.site.register(UserAuthenticationLog, UserAuthenticationLogAdmin)