from django.test import TestCase
from .forms import AboutForm


class TestAboutForm(TestCase):
    def test_about_title_is_required(self):
        form = AboutForm({'title': ''}) 
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors.keys())
        self.assertEqual(form.errors['title'][0], 'This field is required.')

    def test_about_content_is_required(self):
        form = AboutForm({'content': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('content', form.errors.keys())
        self.assertEqual(form.errors['content'][0], 'This field is required.')

    def test_image_field_is_not_required(self):
        form = AboutForm({'title': 'Test About Title', 'content': 'Test About Content'})
        self.assertTrue(form.is_valid())

    def test_fields_are_in_form_metaclass(self):
        form = AboutForm()
        self.assertEqual(form.Meta.fields, ['title', 'content', 'image'])

