from django.urls import path

from .views import LatestPosts, PostList, PostArchives, PostCategories, SearchView, PostDetail

urlpatterns = [
    path('', PostList.as_view(), name='blog_index'),
    path('search/', SearchView.as_view(), name='search'),
    path('archives/', PostArchives.as_view(), name='blog_archives'),
    path('archives/<int:year/', PostArchives.as_view(),
            name='blog_archives'),
    path('categories/', PostCategories.as_view(), name='blog_categories'),
    path('categories/<str:category>/', PostCategories.as_view(),
            name='blog_categories'),
    path('rss/', LatestPosts(), name='blog_rss'),
    path('<slug:slug>/', PostDetail.as_view(), name='blog_detail'),
]
