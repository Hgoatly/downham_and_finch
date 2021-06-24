from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Faq
from .forms import FaqForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator


def faq(request):
    faqs = Faq.objects.all()
    paginator = Paginator(faqs, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'faqs': page_obj,
    }
    return render(request, 'faq/faq.html', context)


@login_required
def add_faq(request):
    if not request.user.is_superuser:
        messages.error(request, "Sorry, you're not authorised do that.")
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = FaqForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added faq!')
            return redirect(reverse('faq'))
        else:
            messages.error(request, 'Faq not added. Please check your form.')
    else:
        form = FaqForm()
    template = 'faq/add_faq.html'
    context = {
        'form': form,
    }
    return render(request, template, context)


@login_required
def delete_faq(request, faq_id):
    """ Delete a faq from the db """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, you are not authorised do that.')
        return redirect(reverse('home'))

    faq = get_object_or_404(Faq, pk=faq_id)
    faq.delete()
    messages.success(request, 'faq deleted!')
    return redirect(reverse('faq'))


@login_required
def edit_faq(request, faq_id):
    """ Edit a faq """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, you are not authorised to do that.')
        return redirect(reverse('home'))

    faq = get_object_or_404(Faq, pk=faq_id)
    if request.method == 'POST':
        form = FaqForm(request.POST, instance=faq)
        if form.is_valid():
            form.save()
            messages.success(request, 'FAQ successfully updated!')
            return redirect(reverse('faq'))
        else:
            messages.error(
                request, 'Unable to update faq. Please check your form.')
    form = FaqForm(instance=faq)
    messages.info(request, f'You are editing {faq.question}')

    template = 'faq/edit_faq.html'
    context = {
        'form': form,
        'faq': faq,
    }

    return render(request, template, context)
