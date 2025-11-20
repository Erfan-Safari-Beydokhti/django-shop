from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class AddPhoneForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['phone']
        widgets = {
            'phone': forms.TextInput(attrs={'class': 'input-text', }),
        }


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'birth_date', 'gender']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'input-text input-text--primary-style', }, ),
            'last_name': forms.TextInput(attrs={'class': 'input-text input-text--primary-style', }),
            'birth_date': forms.DateInput(attrs={'type': 'date', 'class': 'select-box select-box--primary-style', }),
            'gender': forms.Select(attrs={'class': 'select-box select-box--primary-style', }),
        }
        error_messages = {
            'gender': {'required': 'Gender is required.'},
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
