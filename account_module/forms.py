import datetime

from django import forms
from account_module.models import User


import datetime
from django import forms
from account_module.models import User

class RegisterForm(forms.ModelForm):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    YEAR_CHOICES = [(y, y) for y in range(1950, datetime.datetime.now().year + 1)]
    MONTH_CHOICES = [(i, datetime.date(2000, i, 1).strftime('%B')) for i in range(1, 13)]
    DAY_CHOICES = [(d, d) for d in range(1, 32)]

    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password', 'class': 'input-text'})
    )
    gender = forms.ChoiceField(
        choices=GENDER_CHOICES,
        widget=forms.Select(attrs={'class': 'select-box'})
    )
    year = forms.ChoiceField(
        choices=YEAR_CHOICES,
        widget=forms.Select(attrs={'class': 'select-box'})
    )
    month = forms.ChoiceField(
        choices=MONTH_CHOICES,
        widget=forms.Select(attrs={'class': 'select-box'})
    )
    day = forms.ChoiceField(
        choices=DAY_CHOICES,
        widget=forms.Select(attrs={'class': 'select-box'})
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name', 'class': 'input-text'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name', 'class': 'input-text'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'input-text'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'input-text'}),
        }

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not email :
            raise forms.ValidationError("Email is required.")
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError("Email already registered.")
        return email

    def clean_confirm_password(self):
        password = self.cleaned_data.get("password")
        confirm_password = self.cleaned_data.get("confirm_password")
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match!")
        return confirm_password
