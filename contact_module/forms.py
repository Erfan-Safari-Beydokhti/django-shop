from .models import ContactMessages
from django import forms


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessages
        fields = ["subject", "message"]
        widgets = {
            'subject': forms.TextInput(
                attrs={'class': 'input-text input-text--border-radius input-text--primary-style',
                       'placeholder': 'Subject (Required)',}),
            'message': forms.Textarea(attrs={'class': 'text-area text-area--border-radius text-area--primary-style',
                                             'placeholder': 'Compose a Message (Required)','rows': 6}),
        }
