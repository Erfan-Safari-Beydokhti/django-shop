from random import choices

from django import forms
from django.contrib.auth import get_user_model

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
            'first_name': forms.TextInput(attrs={'class': 'input-text input-text--primary-style',}),
            'last_name': forms.TextInput(attrs={'class': 'input-text input-text--primary-style',}),
            'birth_date': forms.DateInput(attrs={'type':'date','class': 'select-box select-box--primary-style',}),
            'gender': forms.Select(attrs={'class': 'select-box select-box--primary-style',}),
        }