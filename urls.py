from django.conf import settings
from django.conf.urls import patterns, url, include
from django.contrib import admin
from django.views.generic import TemplateView

from views import HomeView, ResumeView, BioView, ContactView

admin.autodiscover()
urlpatterns = patterns('',
    url(r'^$', HomeView.as_view(), name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include('apps.blog.urls')),
    url(r'^portfolio/', include('apps.portfolio.urls')),
    url(r'^bio/$', BioView.as_view(), name='bio'),
    url(r'^resume/$', ResumeView.as_view(), name='resume'),
    url(r'^contact/$', ContactView.as_view(), name='contact'),
    url(r'^robots\.txt$', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
)

if not settings.PRODUCTION:
    urlpatterns += patterns('', (r'^files/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}), )
