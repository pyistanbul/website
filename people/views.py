from django.contrib import messages
from django.urls import reverse
from django.views.generic import CreateView, ListView

from people.forms import PersonForm
from people.models import Person


class PeopleView(ListView):
    queryset = Person.objects.active()


class CreatePeopleView(CreateView):
    model = Person
    form_class = PersonForm
    success_message = 'Kişi başarıyla eklendi.'

    def form_valid(self, form):
        messages.success(self.request, self.success_message)
        return super(CreatePeopleView, self).form_valid(form)

    def get_success_url(self):
        return reverse("people:index")
