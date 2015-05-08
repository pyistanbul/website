from django.test import TestCase, Client, override_settings
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.conf import settings

from .models import Post


class PostTest(TestCase):

    dummy_data = {
        'title': 'Hello World',
        'slug': 'hello-world',
        'description': 'First Blog Post',
    }

    def setUp(self):
        self.user = User.objects.create_user(
            username='testpyist', password='123456')
        self.post = Post.objects.create(
            author=self.user, **self.dummy_data)
        self.client = Client()

    def test_detail(self):
        response = self.client.get(self.post.get_absolute_url())
        self.assertContains(response, self.dummy_data['title'])

    def test_list(self):
        response = self.client.get(reverse('blog:home'))
        self.assertContains(response, self.dummy_data['title'])

    def test_invalid_detail(self):
        response = self.client.get(
            reverse('blog:detail', args=['test-test']))
        self.assertEqual(response.status_code, 404)

    def test_pagination(self):
        for i in range(settings.BLOG['LIMIT'] + 1):
            dummy_data = self.dummy_data
            dummy_data['slug'] = dummy_data['slug'] + str(i)
            Post.objects.create(author=self.user, **dummy_data)
        response = self.client.get(reverse('blog:home'))
        self.assertContains(response, "Daha fazla")

    @override_settings(BLOG={
        'TITLE': 'Test Title',
        'DESCRIPTION': 'Python istanbul Test DESCRIPTION',
        'LIMIT': 5,
        'URL': 'http://pyistanbul.org/',
        'DISQUS_USERNAME': 'helevele',
        'USE_DISQUS': True,
    })
    def test_blog_title(self):
        response = self.client.get(reverse('blog:home'))
        self.assertContains(response, "Test Title")

    @override_settings(BLOG={
        'TITLE': 'Python istanbul',
        'DESCRIPTION': 'Python istanbul Test DESCRIPTION',
        'LIMIT': 5,
        'URL': 'http://pyistanbul.org/',
        'DISQUS_USERNAME': 'helevele',
        'USE_DISQUS': True,
    })
    def test_blog_description(self):
        response = self.client.get(reverse('blog:home'))
        self.assertContains(response, "Python istanbul Test DESCRIPTION")

    @override_settings(BLOG={
        'TITLE': 'Python istanbul',
        'DESCRIPTION': 'ython istanbul Gunlugu',
        'LIMIT': 5,
        'URL': 'http://pyistanbul.org/',
        'DISQUS_USERNAME': 'pyistanbul',
        'USE_DISQUS': True,
    })
    def test_use_disqus(self):
        response = self.client.get(self.post.get_absolute_url())
        self.assertContains(response, "http://disqus.com")

    @override_settings(BLOG={
        'TITLE': 'Python istanbul',
        'DESCRIPTION': 'Python istanbul Gunlugu',
        'LIMIT': 5,
        'URL': 'http://pyistanbul.org/',
        'DISQUS_USERNAME': 'helevele',
        'USE_DISQUS': True,
    })
    def test_disqus_username(self):
        response = self.client.get(self.post.get_absolute_url())
        self.assertContains(response, "helevele")
