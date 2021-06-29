from django.test import TestCase


class TestContactViews(TestCase):

    def test_contact_page(self):
        url = '/contact/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact/contact.html')
