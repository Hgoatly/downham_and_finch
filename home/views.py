from django.shortcuts import render


def index(request):
    """ Return the index page. This view
    copied from the Boutique Ado project"""

    return render(request, 'home/index.html')
