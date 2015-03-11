from django.conf.urls import patterns, include, url

from .views import PeopleView, CreatePeopleView


urlpatterns = patterns(
    '',
    url(r'^$', PeopleView.as_view(), name='index'),
    url(r'^new$', CreatePeopleView.as_view(), name='new'),
)
