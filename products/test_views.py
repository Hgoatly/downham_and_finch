from django.test import TestCase
from .models import Product
from django.shortcuts import get_object_or_404

class TestContactViews(TestCase):

    def test_all_products_page(self):
        url = '/products/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    def test_product_detail_page(self, product_id):
        product = Product.objects.create(name='Test Product', pk=product_id)
        response = self.client.get(f'/product/{product.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_detail.html')