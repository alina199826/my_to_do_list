from django import forms
from django.forms import widgets
from webapp.models import Type, Status

class TaskForm(forms.Form):
    summary = forms.CharField(max_length=50, required=True, label='summary')
    status = forms.ModelChoiceField(queryset=Status.objects.all(), label='status')
    description = forms.CharField(max_length=3000, required=True, label='description', widget=widgets.Textarea(attrs={"cols": 20, 'rows': 3}))
    type = forms.ModelMultipleChoiceField(queryset=Type.objects.all(), required=False, label='type')
