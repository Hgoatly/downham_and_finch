from django.test import TestCase
from .forms import BlogForm


class TestBlogForm(TestCase):
    def test_blog_title_is_required(self):
        form = BlogForm({'title': ''}) 
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors.keys())
        self.assertEqual(form.errors['title'][0], 'This field is required.')

    def test_blog_content_is_required(self):
        form = BlogForm({'content': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('content', form.errors.keys())
        self.assertEqual(form.errors['content'][0], 'This field is required.')

    def test_image_field_is_not_required(self):
        form = BlogForm({'title': 'Test Blog Title', 'content': 'Test Blog Content'})
        self.assertTrue(form.is_valid())

    def test_fields_are_in_form_metaclass(self):
        form = BlogForm()
        self.assertEqual(form.Meta.fields, ['title', 'content', 'image'])

