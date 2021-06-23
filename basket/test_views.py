from django.test import TestCase

class TestBasketViews(TestCase):

    def test_basket_page(self):
        url = '/basket/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'basket/basket.html')