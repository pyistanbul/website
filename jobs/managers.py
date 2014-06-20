import datetime

from django.db import models


class JobsManager(models.Manager):

    def active(self):
        now = datetime.datetime.now()
        three_months_ago = now - datetime.timedelta(weeks=3 * 4)
        return super(JobsManager, self).get_query_set().filter(
            date_created__gte=three_months_ago)
