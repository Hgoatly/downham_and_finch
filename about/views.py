from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import About
from .forms import AboutForm


def about(request):
    """ A view to render the 'about' page """

    about = get_object_or_404(About)

    context = {
        'about': about,
    }
    return render(request, 'about/about.html', context)


@login_required
def edit_about(request, about_id):
    """ Edit the 'about' content """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, you are not authorised do that.')
        return redirect(reverse('about'))
    about = get_object_or_404(About, pk=about_id)
    if request.method == 'POST':
        form = AboutForm(request.POST, instance=about)
        if form.is_valid():
            form.save()
            messages.success(request, 'Content successfully updated!')
            return redirect(reverse('about'))
        else:
            messages.error(
                request, 'Unable to update content. Please check your form.')
    form = AboutForm(instance=about)
    messages.info(request, f'You are editing {about.title}')

    template = 'about/edit_about.html'
    context = {
        'form': form,
        'about': about,
    }

    return render(request, template, context)
