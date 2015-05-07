from django.core.urlresolvers import reverse
from django.test import TestCase, Client
from django.contrib.auth.models import User

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

    def test_grouper(self):
        date = '2012-01-%s'
        for i in range(10, 15):
            presentation = self.presentation.copy()
            presentation.update({'date': date % i})
            Presentation.objects.create(**presentation)
        response = self.client.get(reverse('presentations:index'))
        for i in range(10, 15):
            self.assertContains(response, "%s" % date % i)
