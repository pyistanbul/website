from django.core.urlresolvers import reverse
from django.test import TestCase, Client
from django.contrib.auth.models import User

from .models import Job


class JobsTest(TestCase):

    job = {
        'title': 'test title',
        'company': 'test company',
        'url': 'http://example.com',
        'description': 'example description',
        'location': 'istanbul'
    }

    def setUp(self):
        self.tester = User.objects.create(username='tester')
        self.client = Client()

    def test_create(self):
        response = self.client.post(reverse('jobs:new'), self.job)
        self.assertRedirects(response, '/jobs/')
        self.assertTrue(Job.objects.exists())
        job = Job.objects.get()
        self.assertEqual(job.title, 'test title')
        self.assertEqual(job.company, 'test company')
        self.assertEqual(job.url, 'http://example.com/')
        self.assertEqual(job.description.raw, 'example description')
        self.assertEqual(job.location, 'istanbul')

    def test_listing(self):
        job = Job.objects.create(**self.job)
        response = self.client.get(reverse('jobs:detail', args=[job.id]))
        self.assertContains(response, "test title")
