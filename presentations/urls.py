from django.urls import path

from .views import PresentationsView


app_name = "presentations"

urlpatterns = [
    path('', PresentationsView.as_view(), name='index'),
]
