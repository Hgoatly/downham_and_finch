from django import forms
from .models import Faq


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = [
            'title', 'content', 'image'
            ]

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

    placeholders = {
        'title': 'title',
        'content': 'content',
        'image': 'image',
    }