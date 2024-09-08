from django.test import TestCase
from django.test.client import Client


class SampleTest(TestCase):
    def test_translations(self):
        c = Client()
        response = c.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'آمار سایت', html=True, count=2)
