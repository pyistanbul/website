from django.db import models


class PeopleManager(models.Manager):

    def active(self):
        return self.get_queryset().filter(is_active=True)
