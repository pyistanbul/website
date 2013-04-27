from django import forms

from people.models import Person


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ("name", "email", "blog_link", "twitter_username",
                  "github_username")
