from django.shortcuts import render
from django.contrib import messages
from django.urls import reverse
from .forms import suggestPresentationForm
from django.views.generic import CreateView
from .models import suggest

# Create your views here.

class CreateSuggestPresentation(CreateView):
    model = suggest
    form_class = suggestPresentationForm
    success_message = "Öneriniz başarıyla iletildi."

    def form_valid(self, form):
        messages.success(self.request, self.success_message)
        return super(CreateSuggestPresentation, self).form_valid(form)

    def get_success_url(self):
        return reverse("suggestpresentation:index")

