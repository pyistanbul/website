from django.db import models


class JobsManager(models.Manager):

    def active(self):
        return self.get_query_set().filter(is_active=True)

    def live(self):
        return self.active().filter(is_live=True)
