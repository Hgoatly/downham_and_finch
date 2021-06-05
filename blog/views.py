from django.shortcuts import render
from .models import Blog


def blog(request):
    """ A view to render blog posts """

    return render(request, 'blog/blog.html')
