from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.urls import reverse

from .models import Presentation


class PeopleTest(TestCase):

    presentation = {
        'title': 'foo bar',
        'owner': 'edi budu',
        'link': 'http://edibudu.com',
        'description': 'test description',
        'date': '2012-05-15',
    }

    def setUp(self):
        self.tester = User.objects.create(username='tester')
        self.client = Client()

    def test_listing(self):
        Presentation.objects.create(**self.presentation)
        response = self.client.get(reverse('presentations:index'))
        self.assertContains(response, "foo bar")
        self.assertContains(response, "edibudu.com")

    def test_without_link(self):
        presentation_data = self.presentation.copy()
        del presentation_data['link']
        p_without_link = Presentation.objects.create(**presentation_data)
        self.assertIsNone(p_without_link.link)

    def test_grouper(self):
        date = '2012-01-%s'
        for i in range(10, 15):
            presentation = self.presentation.copy()
            presentation.update({'date': date % i})
            Presentation.objects.create(**presentation)
        response = self.client.get(reverse('presentations:index'))
        for i in range(10, 15):
            self.assertContains(response, "%s" % date % i)
