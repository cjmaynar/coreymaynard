from django.conf.urls import patterns, url

from .views import PortfolioList, PortfolioDetail

urlpatterns = patterns('apps.portfolio.views',
    url(r'^$', PortfolioList.as_view(), name='portfolio_index'),
    url(r'^(?P<slug>[-\w]+)/$', PortfolioDetail.as_view(), name='portfolio_detail'),
)
