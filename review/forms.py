from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = [
            'name', 'review'
            ]

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

    placeholders = {
        'name': 'name',
        'review': 'review',
    }