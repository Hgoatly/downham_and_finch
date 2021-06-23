from django.test import TestCase

class TestBlogViews(TestCase):

    def test_blog_page(self):
        url = '/blog/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/blog.html')