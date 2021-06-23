from django.test import TestCase
from django.urls import reverse
from .models import About

class TestAboutViews(TestCase):

    def test_about_page(self):
        about = About.objects.create(title='Test About')
        response = self.client.get(f'/about/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about/about.html')