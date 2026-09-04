from django import forms
from tasks.models import Task

# Django model form
class TaskModelForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'assigned_to']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'w-full p-3 border border-gray-300 rounded-lg',
                'placeholder': 'Enter task title',
            }),

            'description': forms.Textarea(attrs={
                'class': 'w-full p-3 border border-gray-300 rounded-lg',
                'placeholder': 'Enter task description',
                'rows': 4,
            }),

            'due_date': forms.SelectDateWidget(attrs={
                'class': 'p-2 border border-gray-300 rounded-lg',
            }),

            'assigned_to': forms.CheckboxSelectMultiple(attrs={
                'class': 'space-y-2',
            }),
        }

