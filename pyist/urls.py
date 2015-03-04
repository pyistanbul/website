from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.sitemaps.views import index, sitemap

from blog.sitemap import BlogSitemap

admin.autodiscover()

sitemaps = {
    'blog': BlogSitemap,
}

urlpatterns = patterns(
    '',

    # apps
    url(r'^', include('blog.urls', namespace="blog")),
    url(r'^people/', include('people.urls', namespace="people")),
    url(r'^jobs/', include('jobs.urls', namespace="jobs")),
    url(r'^presentations/', include('presentations.urls',
                                    namespace="presentations")),
    url(r'^sitemap\.xml$', index, {'sitemaps': sitemaps}),
    url(r'^sitemap-(?P<section>.+)\.xml$', sitemap, {'sitemaps': sitemaps}),

    # third party apps
    url(r'^comments/', include('djangospam.cookie.urls')),

    # admin
    url(r'^admin/', include(admin.site.urls)),
)
