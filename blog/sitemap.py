from django.contrib.sitemaps import Sitemap

from .models import Post


class BlogSitemap(Sitemap):
    changefreq = "never"
    priority = 0.9

    def items(self):
        return Post.objects.active()

    def lastmod(self, obj):
        return obj.updated_at
