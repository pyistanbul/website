# coding: utf-8

from django.contrib import messages
from django.core.urlresolvers import reverse
from django.views.generic import ListView, CreateView, DetailView

from .models import Job
from .forms import JobForm


class JobsView(ListView):
    queryset = Job.objects.active()


class JobDetailView(DetailView):
    queryset = Job.objects.active()


class CreateJobView(CreateView):
    model = Job
    form_class = JobForm
    success_message = 'İlanınız başarıyle eklendi.'

    def form_valid(self, form):
        messages.success(self.request, self.success_message)
        return super(CreateJobView, self).form_valid(form)

    def get_success_url(self):
        return reverse("jobs:index")
