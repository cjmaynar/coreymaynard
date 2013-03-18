from django.contrib   import messages
from blog.forms       import CommentForm
from django.http      import HttpResponseNotFound
from blog.models      import Post, Category
from django.shortcuts import render_to_response, get_object_or_404
from django.template  import RequestContext


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

    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(approved=True)

    if request.POST:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            if request.user.is_authenticated:
                comment.admin_comment = True
                comment.approved = True
            else:
                comment.admin_comment = False
                comment.approved = False
                
            comment.save()
            messages.success(request, 'Comment saved, awaiting approval')

        else:
            messages.error(request, 'Invalid form, please check and resubmit')
            #Got to do something here to scroll down to the form on error
            for error in form.errors:
                print error
    else:
        form = CommentForm(initial={'post': post.id})

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
        posts = Post.objects.filter(published=True) \
                .filter(categories__name=category)
    else:
        categories = Category.objects.all()

    return render_response(request, "blog/categories.html", vars())
