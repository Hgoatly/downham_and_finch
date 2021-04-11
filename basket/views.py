from django.shortcuts import render


def view_basket(request):
    """ A view that returns the basket contents. 
    This view copied from the Boutique Ado project"""

    return render(request, 'basket/basket.html')
