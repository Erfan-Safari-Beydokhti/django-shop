from importlib.metadata import requires
from random import choices

from django import forms
from django.contrib.auth import get_user_model
from pyexpat.errors import messages

User = get_user_model()
class AddPhoneForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['phone']
        widgets = {
            'phone': forms.TextInput(attrs={'class': 'input-text',}),
        }
        
class EditProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','birth_date','gender']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'input-text input-text--primary-style',},),
            'last_name': forms.TextInput(attrs={'class': 'input-text input-text--primary-style',}),
            'birth_date': forms.DateInput(attrs={'type':'date','class': 'select-box select-box--primary-style',}),
            'gender': forms.Select(attrs={'class': 'select-box select-box--primary-style',}),
        }
        error_messages = {
            'first_name': {
                'required': "Please enter your first name.",
                'max_length': "First name is too long.",
            },
            'last_name': {
                'required': "Please enter your last name.",
                'max_length': "Last name is too long.",
            },
            'birth_date': {
                'required': "Please select your date of birth.",
                'invalid': "Please enter a valid date.",
            },
            'gender': {
                'required': "Please select your gender.",
                'invalid_choice': "Invalid gender selection.",
            },
        }

    def clean_first_name(self):
        fname = self.cleaned_data.get("first_name")
        if not fname or fname.strip() == "":
            raise forms.ValidationError("Please enter your first name.")
        return fname

    def clean_last_name(self):
        lname = self.cleaned_data.get("last_name")
        if not lname or lname.strip() == "":
            raise forms.ValidationError("Please enter your last name.")
        return lname
    def clean_gender(self):
        g = self.cleaned_data.get("gender")
        if not g or g.strip() == "":
            raise forms.ValidationError("Please enter your gender.")
        return g