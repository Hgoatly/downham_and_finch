from django.test import TestCase
from .forms import ReviewForm


class TestReviewForm(TestCase):
    def test_product_is_required(self):
        form = ReviewForm({'product': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('product', form.errors.keys())
        self.assertEqual(form.errors['product'][0], 'This field is required.')

    def test_name_is_required(self):
        form = ReviewForm({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    def test_review_is_required(self):
        form = ReviewForm({'review': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('review', form.errors.keys())
        self.assertEqual(form.errors['review'][0], 'This field is required.')

    def test_fields_are_in_form_metaclass(self):
        form = ReviewForm()
        self.assertEqual(form.Meta.fields, ['product', 'name', 'review'])
