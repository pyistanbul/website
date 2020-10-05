from django.urls import reverse
from django.views.generic import ListView

from people.forms import PersonForm
from people.models import Person


class PeopleView(ListView):
    queryset = Person.objects.active()
    form_class = PersonForm
    success_message = 'Kişi başarıyla eklendi.'

    def get_success_url(self):
        return reverse("people:index")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["page"] = "people"
        context["page_title"] = "İnsanlar"

        return context
