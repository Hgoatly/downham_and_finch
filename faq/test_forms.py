from django.test import TestCase
from .forms import FaqForm


class TestAboutForm(TestCase):
    def test_faq_question_is_required(self):
        form = FaqForm({'question': ''}) 
        self.assertFalse(form.is_valid())
        self.assertIn('question', form.errors.keys())
        self.assertEqual(form.errors['question'][0], 'This field is required.')

    def test_faq_answer_is_required(self):
        form = FaqForm({'answer': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('answer', form.errors.keys())
        self.assertEqual(form.errors['answer'][0], 'This field is required.')

    def test_fields_are_in_form_metaclass(self):
        form = FaqForm()
        self.assertEqual(form.Meta.fields, ['question', 'answer'])

