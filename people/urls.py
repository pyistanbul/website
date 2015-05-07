from django.conf.urls import url

<<<<<<< HEAD
from people.views import PeopleListView, PeopleDetailView
=======
from .views import PeopleView, CreatePeopleView
>>>>>>> 8f9c1ffc25fed2c768cbb5b071480f83f999d174


urlpatterns = [
    url(r'^$', PeopleListView.as_view(), name='index'),
    url(r'^(?P<username>[-\w]+)/$', PeopleDetailView.as_view(), name='detail'),
]
