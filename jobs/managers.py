import datetime

from django.db import models
from django.utils import timezone


class JobsManager(models.Manager):

    def active(self):
        now = timezone.now()
        three_months_ago = now - datetime.timedelta(weeks=3 * 4)

        return super(JobsManager, self).get_queryset().filter(
            is_expired=False, date_created__gte=three_months_ago
        )
