from django.shortcuts import render, redirect


def view_basket(request):
    """ A view that returns the basket contents.
    This view copied from the Boutique Ado project"""

    return render(request, 'basket/basket.html')


def add_to_basket(request, item_id):
    """ A view that adds a quantity of the selected product to the shopping basket.
    This view is copied from the Boutique Ado project."""

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    basket = request.session.get('basket', {})

    if size:
        if item_id in list(basket.keys()):
            if size in basket[item_id]['items_by_size'].keys():
                basket[item_id]['items_by_size'][size] += quantity
            else:
                basket[item_id]['items_by_size'][size] = quantity
        else:
            basket[item_id] = {'items_by_size': {size: quantity}}
    else:
        if item_id in list(basket.keys()):
            basket[item_id] += quantity
        else:
            basket[item_id] = quantity

    request.session['basket'] = basket
    return redirect(redirect_url)
