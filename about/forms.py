from django import forms
from .models import About


class AboutForm(forms.ModelForm):
    class Meta:
        model = About
        fields = [
            'title', 'content', 'image'
            ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black'

    placeholders = {
        'title': 'title',
        'content': 'content',
        'image': 'image',
    }
