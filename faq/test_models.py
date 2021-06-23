from django.test import TestCase
from .models import Faq

class FaqModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up immutable objects to be used by test methods.
        Faq.objects.create(question='New Faq', answer='This is a new question.')

    def test_quesition_label(self):
        faq = Faq.objects.get(id=1)
        field_label = faq._meta.get_field('question').name
        self.assertEqual(field_label, 'question')

    def test_answer_label(self):
        faq = Faq.objects.get(id=1)
        field_label = faq._meta.get_field('answer').name
        self.assertEqual(field_label, 'answer')

    def test_question_max_length(self):
        faq = Faq.objects.get(id=1)
        max_length = faq._meta.get_field('question').max_length
        self.assertEqual(max_length, 200)

    def test_answer_max_length(self):
        faq = Faq.objects.get(id=1)
        max_length = faq._meta.get_field('answer').max_length
        self.assertEqual(max_length, 800)
