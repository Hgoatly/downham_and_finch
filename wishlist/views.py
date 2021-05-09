from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from products.models import Product


def view_wishlist(request):
    """ A view that returns the wishlist contents. """
    wishlist = request.session.get('wishlist', {})

    template = 'wishlist/wishlist.html'
    context = {
        'wishlist': wishlist
    }

    return render(request, template, context)


def add_to_wishlist(request, item_id):
    """ A view to add items to the user's wishlist """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity') or 1)
    my_wishlist = request.session.get('wishlist', {})

    my_wishlist.product.add(product)

    template = 'wishlist/wishlist.html'
    context = {
        'product': product,
        'quantity': quantity,
        'my_wishlist': my_wishlist,
    }

    return render(request, template, context)
