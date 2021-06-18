from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Review
from products.models import Product
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django import forms


def review(request):
    reviews = Review.objects.all().order_by('-date_posted')

    context = {
        'reviews': reviews,
    }
    return render(request, 'review/review.html', context)


@login_required
def add_review(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        form.instance.user = request.user
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added review!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request, 'Review not added. Please check your form.')
    else:
        initial = { 'product': product }
        form = ReviewForm(initial = initial)
        form.fields['product'].widget = forms.HiddenInput()

    template = 'review/add_review.html'
    context = {
        'form': form,
        'product': product,
    }
    return render(request, template, context)


@login_required
def delete_review(request, review_id):
    """ Delete a review from the db """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, you are not authorised do that.')
        return redirect(reverse('home'))

    review = get_object_or_404(Review, pk=review_id)
    review.delete()
    messages.success(request, 'Review deleted!')
    return redirect(reverse('review'))
