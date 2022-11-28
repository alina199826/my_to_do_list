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
        summary = self.cleaned_data['summary']
        if summary == "igil":
            raise ValidationError("These are forbidden words to enter")
        return summary

    def clean_description(self):
        description = self.cleaned_data['description']
        if not " " in description:
            raise ValidationError("Words must be indented'")
        return description


