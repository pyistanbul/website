from django.conf.urls import patterns, include, url

from presentations.views import PresentationsView


urlpatterns = patterns(
    '',
    url(r'^$', PresentationsView.as_view(), name='index'),
)
