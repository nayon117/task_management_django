from django import forms

class TaskForm(forms.Form):
    title = forms.CharField(max_length=250, label='Title')
    description = forms.CharField(widget=forms.Textarea, label='Description')
    due_date = forms.DateField(widget=forms.SelectDateWidget, label='Due Date')
    assigned_to = forms.MultipleChoiceField(widget = forms.CheckboxSelectMultiple, choices = [], label='Assign To')

    def __init__(self, *args, **kwargs):
        employees = kwargs.pop('employees', [])
        print("Employees in form init:", employees)  # Debugging line
        super().__init__(*args, **kwargs)
        self.fields['assigned_to'].choices = [(employee.id, employee.name) for employee in employees]
