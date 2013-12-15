def recent_posts(request):
    '''Get 5 most recent posts from database'''
    from blog.models import Post
    recent = Post.objects.filter(published=True).order_by('-date')[:5]

    return {'recent': recent}

def categories(request):
    '''Get the categories'''
    from blog.models import Category
    from django.db.models import Count
    categories = Category.objects.annotate(num_posts=Count('posts')).order_by('-num_posts')[:5]

    return {'categories': categories}


def is_production(request):
    from settings import PRODUCTION

    return {'is_production': PRODUCTION}
