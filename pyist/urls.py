from django.contrib import admin
from django.contrib.sitemaps.views import index, sitemap
from django.urls import include, path

from blog.sitemap import BlogSitemap

admin.autodiscover()

sitemaps = {
    'blog': BlogSitemap,
}

urlpatterns = [
    # apps
    path('', include('blog.urls')),
    path('people/', include('people.urls')),
    path('presentations/', include('presentations.urls')),
    path('sitemap.xml', index, {'sitemaps': sitemaps}),
    path('sitemap-<section>.xml', sitemap, {'sitemaps': sitemaps}),

    # third party apps
    # path("comments/", include('djangospam.cookie.urls')),

    # admin
    path("admin/", admin.site.urls),
]
