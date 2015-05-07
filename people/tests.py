from django.core.urlresolvers import reverse
from django.test import TestCase, Client
from django.contrib.auth.models import User

from .models import Person


class PeopleTest(TestCase):

    person = {
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

    def test_listing(self):
        Person.objects.create(**self.person)
        response = self.client.get(reverse('people:index'))
        self.assertContains(response, "edi budu")

    def test_active_listing(self):
        person = self.person.copy()
        person['is_active'] = False
        Person.objects.create(**person)
        response = self.client.get(reverse('people:index'))
        self.assertNotContains(response, "edi budu")
