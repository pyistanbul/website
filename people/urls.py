from django.conf.urls import patterns, include, url

from .views import PeopleView


urlpatterns = patterns(
    '',
    url(r'^$', PeopleView.as_view(), name='index')
)
