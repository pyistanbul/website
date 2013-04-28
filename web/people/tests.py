from django.core.urlresolvers import reverse
from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.utils.unittest.case import skip

from people.models import Person


class PeopleTest(TestCase):

    person = {
        'name': 'edi budu',
        'email': 'edi@budu.com',
        'blog_link': 'http://edibudu.com',
        'twitter_username': 'edibudu',
        'github_username': 'edicat'
    }

    def setUp(self):
        self.tester = User.objects.create(username='tester')
        self.client = Client()

    def test_create(self):
        response = self.client.post(reverse('people:new'), self.person)
        self.assertRedirects(response, reverse('people:index'))
        self.assertTrue(Person.objects.exists())
        person = Person.objects.get()
        self.assertEqual(person.name, 'edi budu')
        self.assertEqual(person.email, 'edi@budu.com')
        self.assertEqual(person.blog_link, 'http://edibudu.com/')
        self.assertEqual(person.twitter_username, 'edibudu')
        self.assertEqual(person.github_username, 'edicat')

    def test_listing(self):
        Person.objects.create(**self.person)
        response = self.client.get(reverse('people:index'))
        self.assertContains(response, "edi budu")

    @skip('Confirmation disabled for now')
    def test_active_listing(self):
        person = self.person.copy()
        person['is_active'] = False
        Person.objects.create(**person)
        response = self.client.get(reverse('people:index'))
        self.assertNotContains(response, "edi budu")
