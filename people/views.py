from django.contrib import messages
from django.urls import reverse
from django.views.generic import CreateView, ListView

from people.forms import PersonForm
from people.models import Person
from pyist.mixins import SuccessMessageMixin


class PeopleView(ListView):
    queryset = Person.objects.active()


class CreatePeopleView(SuccessMessageMixin, CreateView):
    model = Person
    form_class = PersonForm
    success_message = 'Kişi başarıyla eklendi.'

    def get_success_url(self):
        return reverse("people:index")
