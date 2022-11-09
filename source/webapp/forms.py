from django import forms
from django.forms import widgets


class TaskForm(forms.Form):
    title = forms.CharField(max_length=50, required=True, label='title')
    deadline = forms.CharField(max_length=50, required=True, label='deadline')
    status = forms.CharField(max_length=20, required=True, label='status')
    description = forms.CharField(max_length=3000, required=True, label='description', widget=widgets.Textarea(attrs={"cols": 20, 'rows': 3}))
