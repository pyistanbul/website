from django.conf.urls import patterns, include, url
from django.contrib import admin

from radpress.views import ArticleListView, ArticleDetailView


admin.autodiscover()

urlpatterns = patterns(
    '',

    # auth
    url(r'^accounts/login/$', 'django.contrib.auth.views.login',
        {'template_name': 'registration/login.html', 'extra_context': {'next': '/wiki'}}),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout',
        {'next_page': '/wiki'}),

    # apps
    url(r'^people/', include('people.urls', namespace="people")),
    url(r'^jobs/', include('jobs.urls', namespace="jobs")),
    url(r'^presentations/', include('presentations.urls',
                                    namespace="presentations")),

    # third party apps
    url(r'^$', ArticleListView.as_view(template_name="index.html"),
        name='home'),
    url(r'^blog/', include('radpress.urls')),
    url(r'^blog/(?P<slug>[-\w]+)$', view=ArticleDetailView.as_view(),
        name='radpress-article-detail'),  # overrides radpress detail url
    url(r'^comments/', include('djangospam.cookie.urls')),

    # wiki
    url(r'^wiki/', include('simplewiki.urls')),

    # admin
    url(r'^admin/', include(admin.site.urls)),
)
