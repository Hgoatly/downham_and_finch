from django import forms
from .models import Product


class CustomProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['display_name']

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
        placeholders = {
            'display_name': 'display_name',
        }



