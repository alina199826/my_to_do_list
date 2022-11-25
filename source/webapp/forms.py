from django import forms
from django.forms import widgets, ValidationError
from webapp.models import Task



class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['summary', 'description', 'status', 'type']
        widgets = {
            'type': widgets.CheckboxSelectMultiple,
        }



    def clean_summary(self):
        cleaned_data = super().clean()
        if cleaned_data['summary'] == "igil":
            raise ValidationError("These are forbidden words to enter")
        return cleaned_data

    def clean_description(self):
        cleaned_data = super().clean()
        if not " " in cleaned_data['description']:
            raise ValidationError("Words must be indented'")
        return cleaned_data


