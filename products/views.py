from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Product_type


def all_products(request):
    """ A view to show all products, including sorting and
    searc queries. This view copied from the Boutique Ado project"""

    products = Product.objects.all()
    query = None
    product_types = None

    if request.GET:
        if 'product_type' in request.GET:
            product_types = request.GET['product_type'].split(',')
            products = products.filter(product_type__name__in=product_types)
            product_types = Product_type.objects.filter(name__in=product_types)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(
                description__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
        'current_product_types': product_types,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details
    This view copied from the Boutique Ado project"""

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)
