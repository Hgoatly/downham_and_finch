from django.test import TestCase
from .models import Product
from django.shortcuts import get_object_or_404

class TestContactViews(TestCase):

    def test_all_products_page(self):
        url = '/products/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    def test_product_detail_page(self, product_id=1):
        
        response = self.client.get(f'/product/1')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_detail.html')