from django.test import TestCase
from .models import Product, Product_type

class Product_typeModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up immutable objects to be used by test methods.
        Product_type.objects.create(name='New_Product', display_name='New Product.')

    def test_product_name_label(self):
        product_type = Product_type.objects.get(id=1)
        field_label = product_type._meta.get_field('name').name
        self.assertEqual(field_label, 'name')

    def test_product_display_name_label(self):
        product_type = Product_type.objects.get(id=1)
        field_label = product_type._meta.get_field('display_name').name
        self.assertEqual(field_label, 'display_name')

    def test_product_name_max_length(self):
        product_type = Product_type.objects.get(id=1)
        max_length = product_type._meta.get_field('name').max_length
        self.assertEqual(max_length, 254)

    def test_product_display_name_max_length(self):
        product_type = Product_type.objects.get(id=1)
        max_length = product_type._meta.get_field('display_name').max_length
        self.assertEqual(max_length, 254)

