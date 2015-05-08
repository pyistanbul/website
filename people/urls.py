from django.conf.urls import url

from .views import PeopleListView, PeopleDetailView


urlpatterns = [
    url(r'^$', PeopleListView.as_view(), name='index'),
    url(r'^(?P<username>[-\w]+)/$', PeopleDetailView.as_view(), name='detail'),
]
