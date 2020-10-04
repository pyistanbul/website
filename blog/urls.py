from django.urls import path

from .views import BlogDetailView, BlogListView
from .feeds import BlogRssFeed, BlogAtomFeed

app_name = 'blog'

urlpatterns = [
    path('', BlogListView.as_view(), name="home"),
    path('blog/<str:slug>', BlogDetailView.as_view(), name="detail"),
    path('feed/rss/', BlogRssFeed(), name="rss-feed"),
    path('feed/atom/', BlogAtomFeed(), name="blog-atom-feed"),
]
