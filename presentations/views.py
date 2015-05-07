from django.views.generic import ListView

from .models import Presentation


class PresentationsView(ListView):
    model = Presentation
