from django.test import TestCase


def test_checkout_page(self):
    response = self.client.get(f'/checkout/')
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'about/about.html')
