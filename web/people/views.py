# coding=utf-8
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.views.generic import ListView, CreateView

from people.models import Person
from people.forms import PersonForm


class PeopleView(ListView):
    model = Person


class CreatePeopleView(CreateView):
    model = Person
    form_class = PersonForm
    success_message = 'Kişi başarıyla eklendi. Editörler tarafından ' \
                      'onaylandıktan sonra sitede yayınlanacaktır.'

    def get_success_url(self):
        messages.success(self.request, self.success_message)
        return reverse("people:index")
