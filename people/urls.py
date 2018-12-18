from django.conf.urls import include, url

from .views import PeopleView, CreatePeopleView


app_name = 'people'


urlpatterns = [
    url(r'^$', PeopleView.as_view(), name='index'),
    url(r'^new$', CreatePeopleView.as_view(), name='new'),
]
