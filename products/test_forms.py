from django.test import TestCase
from .forms import ProductForm

class TestProductForm(TestCase):
    def test_name_is_required(self):
        form = ProductForm({'name': ''}) 
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    def test_product_type_field_is_not_required(self):
            form = ProductForm({'product_type': 'Test Product Type'})
            self.assertTrue(form.is_valid)

