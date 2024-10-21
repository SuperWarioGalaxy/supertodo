from django.forms import ModelForm

from .models import Task


class AddTaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ('name', 'description', 'comple_before')


class EditTaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ('name', 'description', 'done', 'comple_before')
