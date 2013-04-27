# coding=utf-8
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.views.generic import ListView, CreateView

from jobs.models import Job
from jobs.forms import JobForm


class JobsView(ListView):
    model = Job


class CreateJobView(CreateView):
    model = Job
    form_class = JobForm
    success_message = 'İlanınız başarıyle eklendi. Editörler tarafından ' \
                      'onaylandıktan sonra sitede yayınlanacaktır.'

    def get_success_url(self):
        messages.success(self.request, self.success_message)
        return reverse("jobs:index")
