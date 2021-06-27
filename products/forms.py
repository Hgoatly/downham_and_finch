# This file is copied and adapted from Boutique Ado.

from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Product_type


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(
        label='image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        product_types = Product_type.objects.all()
        display_names = [(p.id, p.get_display_name()) for p in product_types]

        self.fields['product_type'].choices = display_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black'
