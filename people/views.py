# coding: utf-8

from django.urls import reverse
from django.views.generic import ListView, CreateView

from people.models import Person
from people.forms import PersonForm
from pyist.mixins import SuccessMessageMixin


class PeopleView(ListView):
    queryset = Person.objects.active()


class CreatePeopleView(SuccessMessageMixin, CreateView):
    model = Person
    form_class = PersonForm
    success_message = 'Kişi başarıyla eklendi.'

    def form_valid(self, form):
        messages.success(self.request, self.success_message)
        return super(PeopleView, self).form_valid(form)

    def get_success_url(self):
        return reverse("people:index")

    def get_context_data(self, **kwargs):
        context = super(PeopleView, self).get_context_data(**kwargs)
        context['page'] = 'people'
        context['page_title'] = 'İnsanlar'
        return context