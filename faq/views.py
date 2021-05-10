from django.shortcuts import render
from .models import Faq


def faq(request):
    faqs = Faq.objects.all()

    context = {
        'faqs': faqs,
    }

    return render(request, 'faq/faq.html', context)
