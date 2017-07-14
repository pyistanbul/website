from django.contrib import messages
from django.core.urlresolvers import reverse
from django.views.generic import ListView, CreateView

from presentations.forms import PresentationRequestForm
from .models import Presentation


class PresentationsView(ListView):
    model = Presentation


class PresentationRequestView(CreateView):
    template_name = 'presentations/presentation_request_form.html'
    form_class = PresentationRequestForm
    success_message = 'Basvurunuz alindi.'

    def form_valid(self, form):
        messages.success(self.request, self.success_message)
        return super(PresentationRequestView, self).form_valid(form)

    def get_success_url(self):
        return reverse("presentations:index")
