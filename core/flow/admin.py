from django.contrib import admin
from .models import WorkFlow, State,Action


# Register your models here.
class WorkFlowAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_by', 'created_at', 'updated_at', 'is_active')
    list_filter = ('created_at', 'updated_at', 'is_active')
    search_fields = ('name', 'created_by__username')
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        (None, {
            'fields': ('name', 'root', 'diagram', 'created_by')
        }),
        ('Status', {
            'fields': ('is_active',),
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
        }),
    )


class StateAdmin(admin.ModelAdmin):
    list_display = ('state', 'team', 'process_percentage', 'action')
    list_filter = ('team', 'action')
    search_fields = ('state', 'team__name', 'action__title')
    list_per_page = 20  # Number of items per admin page



class ActionAdmin(admin.ModelAdmin):
    list_display = ('title', 'next_state')
    list_filter = ('next_state',)
    search_fields = ('title', 'next_state__state')
    list_per_page = 20  # Number of items per admin page



admin.site.register(State, StateAdmin)
admin.site.register(Action, ActionAdmin)
admin.site.register(WorkFlow, WorkFlowAdmin)
