# coding: utf-8
from django.views.generic import ListView, DetailView
from django.contrib.auth.models import User

from .models import Person


class PeopleListView(ListView):
    queryset = Person.objects.active()


class PeopleDetailView(DetailView):
    template_name = "people/person_detail.html"
    queryset = User.objects.filter(is_active=True)
    slug_field = "username"
    slug_url_kwarg = "username"
