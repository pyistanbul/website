from django.test import TestCase, Client
from django.core.urlresolvers import reverse

from .models import Post


class PostTest(TestCase):

    dummy_data = {
        'title': 'Hello World',
        'slug': 'hello-world',
        'description': 'First Blog Post'
    }

    def setUp(self):
        self.post = Post.objects.create(**self.dummy_data)
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
