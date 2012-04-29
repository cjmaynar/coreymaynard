from django.conf.urls.defaults import *
from django.contrib            import admin
from views                     import index

import settings

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include('blog.urls')),
    url(r'^contact/$', 'views.contact', name='contact'),
    url(r'^portfolio/', include('portfolio.urls')),
    url(r'^bio/$', 'views.bio', name='bio'),
    url(r'^resume/$', 'views.resume', name='resume'),
    url(r'^search/$', 'views.search', name='search'),
)

if hasattr(settings, 'MEDIA_ROOT') and not settings.PRODUCTION:
    urlpatterns += patterns('', (r'^files/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}), )
