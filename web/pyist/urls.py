from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.views.generic import TemplateView

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', TemplateView.as_view(template_name="index.html"), name='home'),
    url(r'^people/', include('people.urls', namespace="people")),
    url(r'^jobs/', include('jobs.urls', namespace="jobs")),
    url(r'^presentations/', include('presentations.urls',
                                    namespace="presentations")),
    url(r'^admin/', include(admin.site.urls)),
)
