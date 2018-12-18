from django.conf.urls import include, url
from django.urls import path
from django.contrib import admin
from django.contrib.sitemaps.views import index, sitemap
from django.urls import include, path

from django.conf import settings
from django.conf.urls.static import static

from blog.sitemap import BlogSitemap

admin.autodiscover()

sitemaps = {
    'blog': BlogSitemap,
}

urlpatterns = [
    # apps
    path('', include('blog.urls', namespace="blog")),
    path('people/', include('people.urls')),
    path('presentations/', include('presentations.urls')),
    path('sitemap.xml', index, {'sitemaps': sitemaps}),
    # path('sitemap-(?P<section>.+)\.xml$', sitemap, {'sitemaps': sitemaps}),
    path('sitemap-<section>.xml', sitemap, {'sitemaps': sitemaps}),

    # third party apps
    # path(r'^comments/', include('djangospam.cookie.urls')),
    path('markdownx/', include('markdownx.urls')),

    # admin
    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
