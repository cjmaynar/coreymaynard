from django.conf.urls.defaults import *

urlpatterns = patterns('blog.views',
    url(r'^$', 'blog_index', name='blog_index'),
    url(r'^archives/$', 'blog_archives', name='blog_archives'),
    url(r'^archives/(?P<year>[0-9]{4})/$', 'blog_archives', \
            name='blog_archives'),
    url(r'^categories/(?P<category>\w+)/', 'blog_categories', \
            name='blog_categories'),
    url(r'^(?P<slug>[-\w]+)/', 'blog_detail', name='blog_detail'),
)
