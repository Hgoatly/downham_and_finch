from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Blog


def blog(request):
    """ A view to render blog posts """

    blogs = Blog.objects.all().order_by('-date_posted')

    context = {
        'blogs': blogs,
    }
    return render(request, 'blog/blog.html', context)


@login_required
def deleteBlog(request, blog_id):
    """ Delete a blog post from the db """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, you are not authorised do that.')
        return redirect(reverse('blog'))

    blog = get_object_or_404(Blog, pk=blog_id)
    blog.delete()
    messages.success(request, 'Blog deleted!')
    return redirect(reverse('blog'))
