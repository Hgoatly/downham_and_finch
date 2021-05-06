# This file is copied and adapted from Boutique Ado. 

from django import forms
from .models import Product, Product_type


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        product_types = Product_type.objects.all()
        display_names = [(p.id, p.get_display_name()) for p in product_types]

        self.fields['product_type'].choices = display_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black'


class CustomProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['display_name']

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
        placeholders = {
            'display_name': 'display_name',
        }
