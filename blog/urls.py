from django.urls import path

from .feeds import BlogAtomFeed, BlogRssFeed
from .views import BlogDetailView, BlogListView

app_name = "blog"

urlpatterns = [
    path('', BlogListView.as_view(), name="home"),
    path('blog/<str:slug>/', BlogDetailView.as_view(), name="detail"),
    path('feed/rss/', BlogRssFeed(), name="rss-feed"),
    path('feed/atom/', BlogAtomFeed(), name="blog-atom-feed"),
]
