from django.test import TestCase
from .models import Blog

class BlogModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up immutable objects to be used by test methods.
        Blog.objects.create(title='New Blog', content='This is a new Blog post.')

    def test_title_label(self):
        blog = Blog.objects.get(id=1)
        field_label = blog._meta.get_field('title').name
        self.assertEqual(field_label, 'title')

    def test_content_label(self):
        blog = Blog.objects.get(id=1)
        field_label = blog._meta.get_field('content').name
        self.assertEqual(field_label, 'content')

    def test_title_max_length(self):
        blog = Blog.objects.get(id=1)
        max_length = blog._meta.get_field('title').max_length
        self.assertEqual(max_length, 150)

    def test_content_max_length(self):
        blog = Blog.objects.get(id=1)
        max_length = blog._meta.get_field('content').max_length
        self.assertEqual(max_length, 800)
