from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ValidationError, forms, models


class MyUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(MyUserCreationForm, self).__init__(*args, **kwargs)

        self.fields['email'].required = True


    class Meta(UserCreationForm.Meta):
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name', 'email']

    def clean(self):
        cleaned_data = super().clean()
        if not cleaned_data.get('first_name') and not cleaned_data.get('last_name'):
            raise ValidationError({'first_name': 'Even one of First name or Last name should have a value.'})