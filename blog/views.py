from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.conf import settings

from .models import Post


class BlogListView(ListView):
    template_name = 'index.html'
    queryset = Post.objects.active()
    paginate_by = settings.BLOG['LIMIT']

    def get_context_data(self, **kwargs):
        context = super(BlogListView, self).get_context_data(**kwargs)
        context['page'] = 'home'
        return context


class BlogDetailView(DetailView):
    template_name = "blog/blog_detail.html"
    queryset = Post.objects.active()
