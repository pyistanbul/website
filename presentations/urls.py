from django.conf.urls import url

from .views import PresentationsView


urlpatterns = [
    url(r'^$', PresentationsView.as_view(), name='index'),
]
