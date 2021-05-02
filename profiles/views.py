# This file is copied from the Boutique Ado project

from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .models import UserProfile, DeliveryAddress
from .forms import UserProfileForm, DeliveryAddressForm

from checkout.models import Order


def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)
    delivery_address = DeliveryAddress.objects.all()

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        delivery_form = DeliveryAddressForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        if delivery_form.is_valid():
            delivery_form.save()

    form = UserProfileForm(instance=profile)
    delivery_form = DeliveryAddressForm(request.POST, instance=profile)
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True,
        'delivery_address': delivery_address,
        'delivery_form': delivery_form,
    }

    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
            f'This is a past confirmation for order number {order_number}. '
            'A confirmation email sent was sent on the order date.'
        ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)


def delete_delivery_address(request):
    delivery_address = DeliveryAddress.objects.all()
    template = 'profiles/profile.html'
    if delivery_address:
        delivery_address.delete()

    context = {
        'delivery_form': delivery_address
    }

    return render(request, template, context)



