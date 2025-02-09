from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from django.contrib import admin
from django.views.generic import TemplateView

from views import HomeView, ResumeView, BioView, ContactView

admin.autodiscover()
urlpatterns = [
    path("", HomeView.as_view(), name='index'),
    path("admin/", admin.site.urls),
    path("blog/", include('blog.urls')),
    path("portfolio/", include('portfolio.urls')),
    path("bio/", BioView.as_view(), name='bio'),
    path("resume/", ResumeView.as_view(), name='resume'),
    path("contact/", ContactView.as_view(), name='contact'),
    path("robots\.txt", TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
]

if not settings.PRODUCTION:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns +=     static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

