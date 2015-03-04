from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Atom1Feed
from django.conf import settings

from .models import Post


class BlogRssFeed(Feed):
    title = settings.BLOG['title']
    description = settings.BLOG['description']
    link = settings.BLOG['url']

    def items(self):
        return Post.objects.active()[:20]

    def item_description(self, post):
        return post.description

    def item_pubdate(self, post):
        return post.created_at

    def item_title(self, item):
        return item.title

    def item_link(self, item):
        return item.get_absolute_url()


class BlogAtomFeed(BlogRssFeed):
    feed_type = Atom1Feed
    subtitle = settings.BLOG['description']
