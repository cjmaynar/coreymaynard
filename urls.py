from django.conf.urls import patterns, url, include
from django.contrib            import admin
from django.views.generic import TemplateView

from views                     import index
from settings import PRODUCTION, MEDIA_ROOT

admin.autodiscover()
urlpatterns = patterns('',
    url(r'^$', index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include('blog.urls')),
    url(r'^portfolio/', include('portfolio.urls')),
    url(r'^bio/$', 'views.bio', name='bio'),
    url(r'^resume/$', 'views.resume', name='resume'),
    url(r'^search/$', 'views.search', name='search'),
    url(r'^contact/$', 'views.contact', name='contact'),
    url(r'^robots\.txt$', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
)

if not PRODUCTION:
    urlpatterns += patterns('', (r'^files/(?P<path>.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT}), )
