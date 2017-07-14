from django.conf.urls import url

from .views import PresentationsView, PresentationRequestView

urlpatterns = [
    url(r'^$', PresentationsView.as_view(), name='index'),
    url(r'^apply/$', PresentationRequestView.as_view(), name='request'),
]
