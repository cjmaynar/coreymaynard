from django.contrib.syndication.views import Feed
from django.urls import reverse
from django.db.models import Q
from django.views.generic import ListView, DetailView

from .models import Post, Category


class LatestPosts(Feed):
    title = "Coreymaynard.com Blog"
    link = "/blog/"
    description = "The somewhat frequently updated thoughts of Corey Maynard"

    def items(self):
        return Post.objects.order_by('-date')[:10]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.lead

    def item_link(self, item):
        return reverse('blog_detail', args=[item.slug])


class PostList(ListView):
    template_name = 'blog/index.html'

    def get_queryset(self):
        return Post.objects.filter(published=True)[:10]


class PostDetail(DetailView):
    template_name = 'blog/detail.html'
    model = Post


class PostArchives(ListView):
    template_name = 'blog/archives.html'

    def dispatch(self, request, *args, **kwargs):
        self.year = kwargs.get('year')
        return super(PostArchives, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super(PostArchives, self).get_context_data(*args, **kwargs)
        context.update({
            'year': self.year,
            'years': sorted(set(
                [post.date.year for post in Post.objects.exclude(published=None)]
            ), reverse=True)
        })
        return context

    def get_queryset(self):
        if self.year:
            return Post.objects.filter(published=True).filter(date__year=self.year)
        else:
            return Post.objects.filter(published=True).order_by('-date')


class PostCategories(ListView):
    '''Posts fall into a category, this allows refinement around a topic'''
    template_name = 'blog/categories.html'

    def dispatch(self, request, *args, **kwargs):
        self.category = kwargs.get('category')
        return super(PostCategories, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super(PostCategories, self).get_context_data(*args, **kwargs)
        context['category'] = self.category
        return context

    def get_queryset(self):
        if self.category:
            return Post.objects.filter(published=True).filter(categories__name=self.category)
        else:
            return Category.objects.all()


class SearchView(ListView):
    template_name = 'search.html'

    def dispatch(self, request, *args, **kwargs):
        self.query = request.GET.get('q')
        return super(SearchView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super(SearchView, self).get_context_data(*args, **kwargs)
        context['query'] = self.query
        return context

    def get_queryset(self):
        if self.query:
            return Post.objects.filter(
                Q(title__icontains=self.query) | Q(body__icontains=self.query)
            )
        else:
            return []
