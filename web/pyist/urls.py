from django.conf.urls import patterns, include, url
from django.contrib import admin

from radpress.views import ArticleListView, ArticleDetailView


admin.autodiscover()

urlpatterns = patterns(
    '',

    # apps
    url(r'^people/', include('people.urls', namespace="people")),
    url(r'^jobs/', include('jobs.urls', namespace="jobs")),
    url(r'^presentations/', include('presentations.urls',
                                    namespace="presentations")),

    # third party apps
    url(r'^$', ArticleListView.as_view(template_name="index.html"),
        name='home'),
    url(r'^blog/(?P<slug>[-\w]+)$',view=ArticleDetailView.as_view(),
        name='radpress-article-detail'),

    # admin
    url(r'^admin/',
        include(admin.site.urls)),
)
