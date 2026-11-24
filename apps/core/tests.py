from django.test import TestCase, Client
from django.urls import reverse


class CoreTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_health_check(self):
        response = self.client.get(reverse('health_check'))
        self.assertEqual(response.status_code, 200)
        self.json_data = response.json()
        self.assertEqual(self.json_data['status'], 'healthy')

    def test_homepage_renders(self):
        response = self.client.get(reverse('core:home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "LUXE")
