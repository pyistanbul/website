from django import forms
from .models import suggest

class suggestPresentationForm(forms.ModelForm):
    class Meta:
        model = suggest
        fields = '__all__'