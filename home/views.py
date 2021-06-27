from django.shortcuts import render
from django.views.decorators.clickjacking import xframe_options_exempt


@xframe_options_exempt
def index(request):
    """ Return the index page. This view
    copied from the Boutique Ado project"""

    return render(request, 'home/index.html')
