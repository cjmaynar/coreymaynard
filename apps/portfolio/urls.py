from django.conf.urls.defaults import *

urlpatterns = patterns('portfolio.views',
    url(r'^$', 'portfolio_index', name='portfolio_index'),
    url(r'^(?P<slug>[-\w]+)/$', 'portfolio_detail', name='portfolio_detail'),
)
