from django.conf.urls import url

from .views import BlogDetailView, BlogListView
from .feeds import BlogRssFeed, BlogAtomFeed


urlpatterns = [
    url(r'^$', BlogListView.as_view(), name="home"),
    url(r'^blog/(?P<slug>[-\w]+)/$', BlogDetailView.as_view(),
        name="detail"),
    url(r'^feed/rss/$', BlogRssFeed(), name="rss-feed"),
    url(r'^feed/atom/$', BlogAtomFeed(), name="blog-atom-feed"),
]
