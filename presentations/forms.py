from django.forms import ModelForm

from presentations.models import PresentationRequest


class PresentationRequestForm(ModelForm):
    class Meta:
        model = PresentationRequest
        fields = ('presenter_name', 'presenter_email',
                  'presenter_twitter_username', 'presenter_github_username',
                  'presentation_title', 'presentation_type',
                  'presentation_duration', 'presentation_content')
