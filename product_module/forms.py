from django import forms

from product_module.models import ProductReview


class ReviewForm(forms.ModelForm):
    class Meta:
        model = ProductReview
        fields = ["text", "rating"]
        widgets = {
            'text': forms.Textarea(attrs={'class': 'input-text input-text--primary-style',"placeholder":"Enter review text ..."}),
            'rating':forms.RadioSelect(attrs={'class':''}),
        }
