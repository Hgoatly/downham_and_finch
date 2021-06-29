from django.test import TestCase


class TestReviewViews(TestCase):

    def test_review_page(self):
        url = '/review/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'review/review.html')
