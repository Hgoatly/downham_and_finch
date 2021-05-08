from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from products.models import Product


def view_wishlist(request):
    """ A view that returns the wishlist contents. """

    return render(request, 'wishlist/wishlist.html')


def add_to_wishlist(request, item_id):
    """ A view to add items to the user's wishlist """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity') or 1)
    wishlist = request.session.get('wishlist', {})

    if item_id in list(wishlist.keys()):
        wishlist[item_id] += quantity
        messages.success(request, f'Updated {product.display_name} quantity to {wishlist[item_id]}')
    else:
        wishlist[item_id] = quantity
        messages.success(
            request, f'Added {product.display_name} to your wishlist')

    request.session['wishlist'] = wishlist
    template = 'wishlist/wishlist.html'
    context = {
        'product': product,
        'quantity': quantity,
        'wishlist': wishlist,
    }

    return render(request, template, context)
