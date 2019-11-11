from django.urls import path

from .views import CreatePeopleView, PeopleView

app_name = "people"

urlpatterns = [
    path('', PeopleView.as_view(), name='index'),
    path('new/', CreatePeopleView.as_view(), name='new'),
]
