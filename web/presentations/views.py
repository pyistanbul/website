from django.views.generic import ListView

from presentations.models import Presentation


class PresentationsView(ListView):
    model = Presentation
