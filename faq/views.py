from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Faq
from .forms import FaqForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def faq(request):
    faqs = Faq.objects.all()
    form = FaqForm(request.POST)

    context = {
        'faqs': faqs,
        'form': form
    }
    print(faqs[0].id)
    return render(request, 'faq/faq.html', context)


@login_required
def add_faq(request):
    if not request.user.is_superuser:
        messages.error(request, "Sorry, you're not authorised do that.")
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = FaqForm(request.POST)
        if form.is_valid():
            faq = form.save()
            messages.success(request, 'Successfully added faq!')
            return redirect(reverse('faq', args=[faq.id]))
        else:
            messages.error(request, 'Faq not added. Please check your form.')
    else:
        form = FaqForm(request.POST)
    template = 'faq/faq.html'
    context = {
        'form': form,
    }
    return render(request, template, context)


@login_required
def delete_faq(request, faq_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, you are not authorised do that.')
        return redirect(reverse('home'))

    faq = get_object_or_404(Faq, pk=faq_id)
    faq.delete()
    messages.success(request, 'faq deleted!')
    return redirect(reverse('faq'))
