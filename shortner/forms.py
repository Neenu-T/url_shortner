from django import forms
from .models import Url
class UrlForm(forms.ModelForm):
    class Meta:
        model = Url
        fields = ['original_url']
        widgets = {
            'original_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Enter URL here'})
        }