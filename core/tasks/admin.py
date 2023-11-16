from django.contrib import admin
from .models import (
    Task,
    TaskStatus,
    TaskType,
    TaskComment,
    TaskPriority,
)


# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "creator",
        "type",
        "created_date",
        "last_change",
        "status",
        "assign_to",
        "priority",
    )
    list_filter = (
        "type",
        "status",
        "priority",
        "assign_to",
        "created_date",
        "last_change",
    )

    search_fields = ("title", "creator__email", "assign_to__email")
    readonly_fields = ("created_date", "last_change")

    fieldsets = (
        (
            "Task Information",
            {
                "fields": (
                    "title",
                    "description",
                    "creator",
                    "created_date",
                    "last_change",
                )
            },
        ),
        ("Status", {"fields": ("type", "status", "priority")}),
        ("Assign", {"fields": ("assign_to",)}),
    )
    actions = ["mark_as_done"]

    def mark_as_done(self, request, queryset):
        queryset.update(status=TaskStatus.objects.get(name="Closed"))
        self.message_user(request, f"Selected tasks marked as Done.")

    mark_as_done.short_description = "Mark selected tasks as Done"


class TaskStatusAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
        "created_by",
        "created_at",
        "updated_at",
        "is_active",
    )
    search_fields = ("name", "description", "created_by__email")
    list_filter = ("is_active", "created_at", "updated_at")
    readonly_fields = ("created_at", "updated_at")

    fieldsets = (
        (
            "Task Type Information",
            {
                "fields": (
                    "name",
                    "description",
                    "created_by",
                    "created_at",
                    "updated_at",
                    "is_active",
                )
            },
        ),
    )

    actions = ["toggle_is_active"]

    def toggle_is_active(self, request, queryset):
        for task_type in queryset:
            task_type.is_active = not task_type.is_active
            task_type.save()

        self.message_user(request, f"Selected task types toggled for is_active status.")

    toggle_is_active.short_description = "Toggle is_active status"


class TaskCommentAdmin(admin.ModelAdmin):
    list_display = ("task", "user", "commented_at", "attachments")
    list_filter = ("task", "user", "commented_at")
    search_fields = ("task__title", "user__email", "comment")
    readonly_fields = ("commented_at",)

    fieldsets = (
        (
            "Comment Information",
            {"fields": ("task", "user", "comment", "commented_at", "attachments")},
        ),
    )


admin.site.register(Task, TaskAdmin)
admin.site.register(TaskType, TaskStatusAdmin)
admin.site.register(TaskStatus, TaskStatusAdmin)
admin.site.register(TaskComment, TaskCommentAdmin)
admin.site.register(TaskPriority, TaskStatusAdmin)
