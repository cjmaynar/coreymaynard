from django.conf import settings
from django.db.models import Count

from apps.blog.models import Post, Category


def recent_posts(request):
    '''Get 5 most recent posts from database'''
    recent = Post.objects.filter(published=True).order_by('-date')[:5]
    return {'recent': recent}


def categories(request):
    '''Get the categories'''
    categories = Category.objects.annotate(num_posts=Count('posts')).order_by('-num_posts')[:5]
    return {'categories': categories}


def is_production(request):
    return {'is_production': settings.PRODUCTION}
