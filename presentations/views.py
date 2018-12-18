from django.views.generic import ListView

from .models import Presentation


class PresentationsView(ListView):
    model = Presentation

    def get_context_data(self, **kwargs):
        context = super(PresentationsView, self).get_context_data(**kwargs)
        context['page'] = 'presentation'
        context['page_title'] = 'Sunumlar'
        return context