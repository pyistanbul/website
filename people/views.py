# coding: utf-8

from django.urls import reverse
from django.views.generic import ListView, CreateView

from pyist.mixins import SuccessMessageMixin
from people.models import Person
from people.forms import PersonForm


class PeopleView(ListView):
    queryset = Person.objects.active()


class CreatePeopleView(SuccessMessageMixin, CreateView):
    model = Person
    form_class = PersonForm
    success_message = 'Kişi başarıyla eklendi.'

    def get_success_url(self):
        return reverse("people:index")
