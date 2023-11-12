from django import forms
from .models import Task, TaskStatus


class CreateTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ("title", "description", "type", "status", "assign_to", "priority")

class CreateTaskStatusForm(forms.ModelForm):
    class Meta:
        model = TaskStatus
        fields = ("name", "description",)
