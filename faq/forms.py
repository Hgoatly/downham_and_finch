from django import forms
from .models import Faq


class FaqForm(forms.ModelForm):
    class Meta:
        model = Faq
        fields = [
            'question', 'answer'
            ]

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

        placeholders = {
            'question': 'question',
            'answer': 'answer',
        }
