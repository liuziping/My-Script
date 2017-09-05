# encoding: utf-8
from django import forms
from .models import AutoTasks, ExecResult


class TaskAddForm(forms.ModelForm):
    class Meta:
        model = AutoTasks
        fields = ['name', 'playbook']
