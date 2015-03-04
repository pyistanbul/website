from django.db import models


class BlogManager(models.Manager):

    def active(self):
        return super(BlogManager, self).get_query_set().filter(
            is_published=True)

    def passive(self):
        return super(BlogManager, self).get_query_set().filter(
            is_published=False)
