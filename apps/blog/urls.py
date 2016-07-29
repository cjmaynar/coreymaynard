from django.conf.urls import patterns, url

from .views import LatestPosts, PostList, PostArchives, PostCategories, SearchView, PostDetail

urlpatterns = patterns('apps.blog.views',
    url(r'^$', PostList.as_view(), name='blog_index'),
    url(r'^search/$', SearchView.as_view(), name='search'),
    url(r'^archives/$', PostArchives.as_view(), name='blog_archives'),
    url(r'^archives/(?P<year>[0-9]{4})/$', PostArchives.as_view(), \
            name='blog_archives'),
    url(r'^categories/$', PostCategories.as_view(), name='blog_categories'),
    url(r'^categories/(?P<category>\w+)/', PostCategories.as_view(), \
            name='blog_categories'),
    url(r'^rss/$', LatestPosts(), name='blog_rss'),
    url(r'^(?P<slug>[-\w]+)/', PostDetail.as_view(), name='blog_detail'),
)
