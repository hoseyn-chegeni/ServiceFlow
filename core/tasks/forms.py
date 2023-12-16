from django import forms
from .models import Task, TaskStatus, TaskType, TaskPriority, TaskLogFlow


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






class TaskLogFlowForm(forms.ModelForm):
    class Meta:
        model = TaskLogFlow
        fields = ['task', 'comment', 'attachments_1', 'attachments_2', 'attachments_3', 'action']
        
    def __init__(self, *args, **kwargs):
        initial = kwargs.get('initial', {})
        task = initial.get('task')
        if task:
            super(TaskLogFlowForm, self).__init__(*args, **kwargs)
            self.fields['action'].queryset = task.actions.all()
        else:
            super(TaskLogFlowForm, self).__init__(*args, **kwargs)