from django.conf.urls import url

from .views import PresentationsView


app_name = 'presentations'


urlpatterns = [
    url(r'^$', PresentationsView.as_view(), name='index'),
]
