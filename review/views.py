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
