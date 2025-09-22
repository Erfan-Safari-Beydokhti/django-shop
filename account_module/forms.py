import datetime

from django import forms
from django.contrib.auth.models import User


class RegisterForm(forms.ModelForm):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    YEAR_CHOICES = [(y, y) for y in range(1950, datetime.datetime.now().year + 1)]

    MONTH_CHOICES = [(i, datetime.date(2000, i, 1).strftime('%B')) for i in range(1, 13)]
    DAY_CHOICES = [(d, d) for d in range(1, 32)]

    confirm_password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'input-text input-text--primary-style', 'placeholder': 'Confirm Password'}))

    gender = forms.ChoiceField(choices=GENDER_CHOICES,
                               widget=forms.Select(attrs={'class': 'select-box select-box--primary-style u-w-100'}))

    year = forms.ChoiceField(choices=YEAR_CHOICES, widget=forms.Select(
        attrs={'class': 'select-box select-box--primary-style', 'placeholder': 'Year'}))
    month = forms.ChoiceField(choices=MONTH_CHOICES, widget=forms.Select(
        attrs={'class': 'select-box select-box--primary-style', 'placeholder': 'Month'}))
    day = forms.ChoiceField(choices=DAY_CHOICES, widget=forms.Select(
        attrs={'class': 'select-box select-box--primary-style', 'placeholder': 'Day'}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'input-text input-text--primary-style',
                'placeholder': 'First Name',
                'id': 'reg-fname',
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'input-text input-text--primary-style',
                'placeholder': 'Last Name',
                'id': 'reg-lname',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'input-text input-text--primary-style',
                'placeholder': 'Enter E-mail',
                'id': 'reg-email',
            }),
            'password': forms.PasswordInput(attrs={
                'class': 'input-text input-text--primary-style',
                'placeholder': 'Enter Password',
                'id': 'reg-password',
            }),
        }

    def clean_confirm_password(self):
        password = self.cleaned_data.get("password")
        confirm_password = self.cleaned_data.get("confirm_password")
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match!")
        return confirm_password

    def save(self, commit=True):
        user = super().save(commit=False)
        y = int(self.cleaned_data['year'])
        m = int(self.cleaned_data['month'])
        d = int(self.cleaned_data['day'])
        user.birth_date = datetime.date(y, m, d)

        user.username = self.cleaned_data['email']
        user.set_password(self.cleaned_data['password'])

        if commit:
            user.save()
        return user
