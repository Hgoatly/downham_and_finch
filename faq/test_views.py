from django.test import TestCase

class TestFaqViews(TestCase):

    def test_about_page(self):
        url = '/faq/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'faq/faq.html')