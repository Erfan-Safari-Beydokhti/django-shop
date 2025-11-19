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