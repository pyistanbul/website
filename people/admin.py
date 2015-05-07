from django.contrib import admin

from people.models import Person, SocialAccountLink


admin.site.register(Person)
admin.site.register(SocialAccountLink)
