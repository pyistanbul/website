from django.conf.urls import include, url

from .views import PeopleView


app_name = 'people'


urlpatterns = [
    url(r'^$', PeopleView.as_view(), name='index'),
]