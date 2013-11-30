from django.db import models


class PeopleManager(models.Manager):

    def active(self):
        return self.get_query_set().filter(is_active=True)

