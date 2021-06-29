from django.test import TestCase
from .models import Product
from django.shortcuts import get_object_or_404

class TestProductViews(TestCase):

    def test_all_products_page(self):
        url = '/products/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')
