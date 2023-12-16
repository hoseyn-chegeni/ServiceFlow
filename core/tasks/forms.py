from django import forms
from .models import Task, TaskStatus, TaskType, TaskPriority


class CreateTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ("title", "description", "type", "priority")


class CreateTaskStatusForm(forms.ModelForm):
    class Meta:
        model = TaskStatus
        fields = (
            "name",
            "description",
        )


class CreateTaskTypeForm(forms.ModelForm):
    class Meta:
        model = TaskType
        fields = (
            "name",
            "description",
        )


class CreateTaskPriorityForm(forms.ModelForm):
    class Meta:
        model = TaskPriority
        fields = (
            "name",
            "description",
            "badge",
        )
