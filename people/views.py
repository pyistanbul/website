# coding: utf-8

from django.contrib import messages
from django.core.urlresolvers import reverse
from django.views.generic import ListView, CreateView

from people.models import Person
from people.forms import PersonForm


class PeopleView(ListView):
    queryset = Person.objects.active()


class CreatePeopleView(CreateView):
    model = Person
    form_class = PersonForm
    success_message = (
        'Kişi başarıyla eklendi. Editörler tarafından '
        'onaylandıktan sonra sitede yayınlanacaktır.'
    )

    def form_valid(self, form):
        messages.success(self.request, self.success_message)
        return super(CreatePeopleView, self).form_valid(form)

    def get_success_url(self):
        return reverse("people:index")
