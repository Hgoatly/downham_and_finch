from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import About


def about(request):
    """ A view to render the 'about' page """

    about = get_object_or_404(About)

    context = {
        'about': about,
    }
    return render(request, 'about/about.html', context)



def edit_about():
    pass


