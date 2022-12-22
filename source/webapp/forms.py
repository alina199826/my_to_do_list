from django import forms
from django.forms import widgets, ValidationError
from webapp.models import Task, Project



class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['summary', 'description', 'status', 'type', 'project']
        widgets = {
            'type': widgets.CheckboxSelectMultiple,
        }



    def clean_summary(self):
        summary = self.cleaned_data['summary']
        if summary == "igil".upper():
            raise ValidationError("These are forbidden words to enter")
        return summary

    def clean_description(self):
        description = self.cleaned_data['description']
        if not " " in description:
            raise ValidationError("Words must be indented'")
        return description



class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'content', 'date_start', 'date_end', 'users']

        widgets = {
            'users': widgets.CheckboxSelectMultiple,
        }


class TaskDeleteForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['summary']

    def clean_summary(self):
        title = self.cleaned_data['summary']
        if self.instance.title != title:
            raise ValidationError("Names don't match")
        return title

class ProjectDeleteForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title']

    def clean_title(self):
        title2 = self.cleaned_data['title']
        if self.instance.title != title2:
            raise ValidationError("Names don't match")
        return title2


class SimpleSearchForm(forms.Form):
    search = forms.CharField(max_length=50, required=False, label='поиск')