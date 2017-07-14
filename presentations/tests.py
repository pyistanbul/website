from django.core.urlresolvers import reverse
from django.test import TestCase, Client
from django.contrib.auth.models import User

from presentations.views import PresentationRequestView
from .models import Presentation, PresentationRequest


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

    def test_request_form(self):
        self.path = reverse('presentations:request')
        form_data = {"presenter_name": "ali bey", "presenter_email": "a@b.com",
                     "presenter_twitter_username": "@ali",
                     "presenter_github_username": "@ali",
                     "presentation_title": "django 2.1",
                     "presentation_type": "sunum",
                     "presentation_duration": "30",
                     "presentation_content": "will be fun.",
                     }
        response = self.client.post(self.path, form_data)
        print(response.content)
        self.assertEqual(response.status_code, 302)
        pr = PresentationRequest.objects.get()
        self.assertEquals(pr.presenter_name, 'ali bey')
        self.assertEquals(pr.presenter_email, 'a@b.com')
        self.assertEquals(pr.presenter_twitter_username, '@ali')
        self.assertEquals(pr.presenter_github_username, '@ali')
        self.assertEquals(pr.presentation_title, 'django 2.1')
        self.assertEquals(pr.presentation_type, 'sunum')
        self.assertEquals(pr.presentation_duration, 30)
        self.assertEquals(pr.presentation_content, 'will be fun.')
