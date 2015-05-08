# coding: utf-8
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

    def test_people_detail(self):
        response = self.client.get(
            reverse('people:detail', args=[self.tester.username]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.tester.username)

    def test_people_detail_passive_user(self):
        self.tester.is_active = False
        self.tester.save()
        response = self.client.get(
            reverse('people:detail', args=[self.tester.username]))
        self.assertEqual(response.status_code, 404)

    def test_people_detail_not_found(self):
        response = self.client.get(
            reverse('people:detail', args=["test123"]))
        self.assertEqual(response.status_code, 404)

    def test_people_detail_method_not_allowed(self):
        response = self.client.post(
            reverse('people:detail', args=[self.tester.username]))
        self.assertEqual(response.status_code, 405)

    def test_people_detail_password_change_link(self):
        self.tester.set_password('123456')
        self.tester.save()
        self.client.login(username=self.tester.username, password='123456')
        response = self.client.get(
            reverse('people:detail', args=[self.tester.username]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.tester.username)
        self.assertContains(response, u"Parola Değiştir")
