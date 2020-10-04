from django.urls import path

from .views import PeopleView

app_name = "people"

urlpatterns = [
    path('', PeopleView.as_view(), name='index'),
]
