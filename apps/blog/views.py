from django.shortcuts import render_to_response, get_object_or_404
from django.template  import RequestContext
from blog.models      import Post
from blog.forms       import CommentForm
from django.http      import HttpResponseNotFound


def render_response(request, *args, **kwargs):
    '''Custom render_to_response wrapper to contain the blog_processor
    function'''
    kwargs['context_instance'] = RequestContext(request,
        processors=(blog_processor,)
    )

    return render_to_response(*args, **kwargs)


def blog_processor(request):
    '''Add some extra stuff on every page'''
    posts = Post.objects.exclude(published=None)
    years = []

    for post in posts:
        years.append(post.date.year)

    years = sorted(set(years), reverse=True)

    return {
        'years': years,
    }


def blog_index(request):
    '''The landing page of the blog'''
    try:
        posts = Post.objects.filter(published=True)[:10]
        return render_response(request, "blog/index.html", vars())
    except:
        return HttpResponseNotFound


def blog_detail(request, slug):
    '''View a specific post'''
    from settings import MEDIA_URL

    post     = get_object_or_404(Post, slug=slug)
    comments = post.comments

    if request.POST:
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            #Got to do something here to scroll down to the form on error
            for error in form.errors:
                print error
    else:
        form = CommentForm(initial={'post':post.id})

    return render_response(request, "blog/detail.html", vars())


def blog_archives(request, year=None):
    '''A collection of all the posts that have been made'''
    if year:
        archives = Post.objects.filter(published=True).filter(date__year=year)
    else:
        archives = Post.objects.filter(published=True).order_by('-date')

    return render_response(request, "blog/archives.html", vars())


def blog_categories(request, category=None):
    '''Posts fall into a category, this allows refinement around a topic'''
    if category:
        posts = Post.objects.filter(published=True).filter(categories__name=category)
    else:
        posts = Post.objects.filter(published=True)

    return render_response(request, "blog/categories.html", vars())
