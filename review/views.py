from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Review
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def review(request):
    reviews = Review.objects.all()

    context = {
        'reviews': reviews,
    }
    return render(request, 'review/review.html', context)


@login_required
def add_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added review!')
            return redirect(reverse('review'))
        else:
            messages.error(
                request, 'Review not added. Please check your form.')
    else:
        form = ReviewForm()
    template = 'review/add_review.html'
    context = {
        'form': form,
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
