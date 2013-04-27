from django import forms

from jobs.models import Job


class JobForm(forms.ModelForm):
    class Meta:
        model = Job