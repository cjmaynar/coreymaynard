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
