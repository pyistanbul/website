from django.views.generic import ListView, TemplateView
from django.views.generic.detail import DetailView
from django.conf import settings

from .models import Post


class BlogListView(ListView):
    template_name = 'index.html'
    queryset = Post.objects.active()
    paginate_by = settings.BLOG['LIMIT']


class BlogDetailView(DetailView):
    template_name = "blog/blog_detail.html"
    queryset = Post.objects.active()


class HakkimizdaView(TemplateView):
    template_name = "hakkimizda.html"
