from django.contrib.auth.models import User
from django.test import TestCase

from .models import Post


class PostModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # FIXME: Replace with model factory
        user = User.objects.create(
            username="testuser",
            password="123456",
        )

        # FIXME: Replace with model factory
        Post.objects.create(
            author=user,
            title="Hello Blog",
            slug="hello-blog",
            description="First Blog Post Hede"
        )

    def test_get_absolute_url(self):
        post = Post.objects.get(id=1)
        self.assertEquals(post.get_absolute_url(), '/blog/hello-blog/')

    def test_title_max_length(self):
        post = Post.objects.get(id=1)
        max_length = post._meta.get_field('title').max_length
        self.assertEquals(max_length, 255)

    def test_slug_max_length(self):
        post = Post.objects.get(id=1)
        max_length = post._meta.get_field('slug').max_length
        self.assertEquals(max_length, 255)


# class PostViewTest(TestCase):
#     @classmethod
#     def setUpTestData(cls):
#         test_user = User.objects.create(username='testuser', password='123456')
#         test_user.save()

#         number_of_posts = 10
#         for post_num in range(number_of_posts):
#             Post.objects.create(author=test_user,
#                                 title="Hello Blog %s" % post_num,
#                                 slug="hello-blog-%s" % post_num,
#                                 description="First Blog Post %s" % post_num)

#     def test_detail(self):
#         response = self.client.get(self.post.get_absolute_url())
#         self.assertContains(response, self.post.slug)



# class PostTest(TestCase):

#     dummy_data = {
#         'title': 'Hello Blog',
#         'slug': 'hello-blog',
#         'description': 'First Blog Post Blog',
#     }

#     def setUp(self):
#         self.user = User.objects.create_user(
#             username='testpyistanbul', password='123456')
#         self.post = Post.objects.create(
#             author=self.user, **self.dummy_data)
#         self.client = Client()

#     def test_detail(self):
#         response = self.client.get(self.post.get_absolute_url())
#         print("=================")
#         print(response)
#         print("=================")
#         self.assertContains(response, self.dummy_data['slug'])

#     def test_list(self):
#         response = self.client.get(reverse('blog:home'))
#         self.assertContains(response, self.dummy_data['title'])

#     def test_valid(self):
#         response = self.client.get(reverse('blog:detail', args=['hello-blog']))
#         self.assertEqual(response.status_code, 200)

#     def test_invalid_detail(self):
#         response = self.client.get(
#             reverse('blog:detail', args=['test-test']))
#         self.assertEqual(response.status_code, 404)
