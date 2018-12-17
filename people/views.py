from django.urls import reverse
from django.views.generic import ListView

from people.forms import PersonForm
from people.models import Person


class PeopleView(ListView):
    queryset = Person.objects.active()


class PeopleView(ListView):
    model = Person
    form_class = PersonForm
    success_message = 'Kişi başarıyla eklendi.'

    def get_success_url(self):
        return reverse("people:index")
