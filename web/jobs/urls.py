from django.conf.urls import patterns, url

from jobs.views import JobsView, CreateJobView


urlpatterns = patterns(
    '',
    url(r'^$', JobsView.as_view(), name='index'),
    url(r'^new$', CreateJobView.as_view(), name='new'),
)
