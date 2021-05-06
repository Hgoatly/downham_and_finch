from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Product_type, FabricChoice
from .forms import CustomProductForm


def all_products(request):
    """ A view to show all products, including sorting and
    search queries. This view copied from the Boutique Ado project"""

    products = Product.objects.all()
    fabric_choice = FabricChoice.objects.all()
    query = None
    product_types = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'product_type':
                sortkey = 'product_type__name'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'

            products = products.order_by(sortkey)

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
    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_product_types': product_types,
        'current_sorting': current_sorting,
        'fabric_choice': fabric_choice,
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


def custom_products(request):

    products = Product.objects.filter(product_type__id=7)
    fabrics = FabricChoice.objects.all()
    form = CustomProductForm

    context = {
        'products': products,
        'fabrics': fabrics,
        'form': form,
    }

    return render(request, 'products/custom_products.html', context)


def fabric_detail(request, fabric_id):
    fabric = get_object_or_404(FabricChoice, id=fabric_id)
    products = Product.objects.filter(product_type__id=7)

    context = {
        'fabric': fabric,
        'products': products,
    }

    return render(request, 'products/fabric_detail.html', context)

