from django.conf.urls import include, url
from .views import CreateSuggestPresentation

app_name = 'suggestpresentation'

urlpatterns = [
    url('', CreateSuggestPresentation.as_view(), name="index"),
]