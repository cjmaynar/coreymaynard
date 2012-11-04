def grooveshark(request):
    '''Grab feed from Groveshark, format, and return 5 most recent songs
    Cached using localmemory
    Used as a Context Processor accross the entire site'''
    from django.core.cache import cache
    import feedparser

    try:
        feed = 'http://api.grooveshark.com/feeds/1.0/users/cjmaynar/recent_listens.rss'
        data = cache.get(feed)
        if not data:
            data = feedparser.parse(feed)
            cache.set(feed, data)

        songs = []
        for i in range(0, 5):
            songs.append({
                'title': data.entries[i].title,
                'link': data.entries[i].link
            })

        return {'songs': songs}
    except:
        #Can't get cache or feed...
        return {'songs': ''}


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
