from django import forms
from django.forms import widgets
from webapp.models import Type, Status

class TaskForm(forms.Form):
    summary = forms.CharField(max_length=50, required=True, label='summary')
    type = forms.ModelChoiceField(queryset=Type.objects.all(), required=True, label='type')
    status = forms.ModelChoiceField(queryset=Status.objects.all(), required=True, label='status')
    # created_at = forms.DateTimeField(label='created_date')
    # updated_at = forms.DateTimeField(label='updated_date')
    description = forms.CharField(max_length=3000, required=True, label='description', widget=widgets.Textarea(attrs={"cols": 20, 'rows': 3}))
