from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Blog
from .forms import BlogForm


def blog(request):
    """ A view to render blog posts """

    blogs = Blog.objects.all().order_by('-date_posted')

    context = {
        'blogs': blogs,
    }
    return render(request, 'blog/blog.html', context)


def blog_detail(request, blog_id):
    """ A view to show individual blog entries. """

    blog = get_object_or_404(Blog, pk=blog_id)

    context = {
        'blog': blog,
    }
    print(context)

    return render(request, 'blog/blog_detail.html', context)



def add_blog(request):
    if not request.user.is_superuser:
        messages.error(request, "Sorry, you're not authorised do that.")
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added post!')
            return redirect(reverse('blog'))
        else:
            messages.error(request, 'Post not added. Please check your form.')
    else:
        form = BlogForm()
    template = 'blog/add_blog.html'
    context = {
        'form': form,
    }
    return render(request, template, context)


@login_required
def delete_blog(request, blog_id):
    """ Delete a blog post from the db """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, you are not authorised do that.')
        return redirect(reverse('blog'))

    blog = get_object_or_404(Blog, pk=blog_id)
    blog.delete()
    messages.success(request, 'Blog deleted!')
    return redirect(reverse('blog'))
