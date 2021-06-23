from django.test import TestCase
from .forms import ProductForm

class TestProductForm(TestCase):
    def test_name_is_required(self):
        form = ProductForm({'name': ''}) 
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    def test_sku_is_required(self):
        form = ProductForm({'sku': ''}) 
        self.assertFalse(form.is_valid())
        self.assertIn('sku', form.errors.keys())
        self.assertEqual(form.errors['sku'][0], 'This field is required.')

    def test_description_is_required(self):
        form = ProductForm({'description': ''}) 
        self.assertFalse(form.is_valid())
        self.assertIn('description', form.errors.keys())
        self.assertEqual(form.errors['description'][0], 'This field is required.')

    def test_price_is_required(self):
        form = ProductForm({'price': ''}) 
        self.assertFalse(form.is_valid())
        self.assertIn('price', form.errors.keys())
        self.assertEqual(form.errors['price'][0], 'This field is required.')

    def test_product_type_field_is_not_required(self):
            form = ProductForm({'product_type': 'Test Product Type'})
            self.assertTrue(form.is_valid)

    def test_display_name_field_is_not_required(self):
            form = ProductForm({'product_type': 'Test Product Type', 'sku': 'Test Sku', 
                                'name': 'Test Name', 'display_name': 'Test Display Name'})
            self.assertTrue(form.is_valid)

    def test_colour_field_is_not_required(self):
            form = ProductForm({'product_type': 'Test Product Type', 'sku': 'Test Sku', 
                            'name': 'Test Name', 'display_name': 'Test Display Name',
                            'colour': 'Test Colour'})
            self.assertTrue(form.is_valid)

    def test_has_sizes_field_is_not_required(self):
            form = ProductForm({'has_sizes': 'Test Sizes'})
            self.assertTrue(form.is_valid)

    def test_display_name_field_is_not_required(self):
            form = ProductForm({'display_name': 'Test Display Name'})
            self.assertTrue(form.is_valid)

    def test_quantity_in_pack_field_is_not_required(self):
            form = ProductForm({'quantity_in_pack': 'Test Quantity in Pack'})
            self.assertTrue(form.is_valid)

    def test_image_field_is_not_required(self):
            form = ProductForm({'image': 'Test Image'})
            self.assertTrue(form.is_valid)

    def test_fields_are_in_form_metaclass(self):
        form = ProductForm()
        self.assertEqual(form.Meta.fields, ('__all__'))


