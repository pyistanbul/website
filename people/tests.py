from unittest import skip

from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.urls import reverse

from .models import Person


class PeopleTest(TestCase):
    test_data = {
        'name': 'edi budu',
        'email': 'edi@budu.com',
        'blog_link': 'http://edibudu.com',
        'twitter_username': 'edibudu',
        'github_username': 'edicat',
        'is_active': True,
    }

    def setUp(self):
        self.tester = User.objects.create(username='tester')
        self.client = Client()

    @skip
    def test_create(self):
        response = self.client.post(reverse('people:new'), self.test_data)
        self.assertRedirects(response, reverse('people:index'))
        self.assertTrue(Person.objects.exists())

        person = Person.objects.get()
        self.assertEqual(person.name, 'edi budu')
        self.assertEqual(person.email, 'edi@budu.com')
        self.assertEqual(person.blog_link, 'http://edibudu.com')
        self.assertEqual(person.twitter_username, 'edibudu')
        self.assertEqual(person.github_username, 'edicat')

    def test_listing(self):
        Person.objects.create(**self.test_data)
        response = self.client.get(reverse('people:index'))
        self.assertContains(response, "edi budu")

    def test_active_listing(self):
        data = self.test_data.copy()
        data["is_active"] = False
        Person.objects.create(**data)

        response = self.client.get(reverse("people:index"))

        self.assertNotContains(response, "edi budu")
