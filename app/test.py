from django.test import (TestCase, Client)

from app.models import URLMapper


class TestURLMapper(TestCase):
    fixtures = ["url_mapper.json"]

    def setUp(self):
        self.client = Client()

    def test_status_code_fetch_urls(self):
        response = self.client.get('/urls/')
        self.assertEqual(response.status_code, 200)  # Accept

    def test_status_code_fetch_url(self):
        response = self.client.get('/1')
        self.assertEqual(response.status_code, 302)  # Redirect

    def test_status_code_add_url_valid(self):
        response = self.client.post('/urls/', {"url": "https://example.com"})
        self.assertEqual(response.status_code, 201)  # Created

    def test_status_code_add_url_invalid(self):
        response = self.client.post('/urls/', {"url": "55555"})
        self.assertEqual(response.status_code, 400)  # Bad Request

    def test_add_url(self):
        self.client.post('/urls/', {"url": "https://example.com"})
        objects = URLMapper.objects.filter(url="https://example.com")
        self.assertEqual(len(objects), 1)
        self.assertEqual(objects[0].url, "https://example.com")

    def test_get_urls(self):
        response = self.client.get('/urls/?limit=10')
        self.assertEqual(len(response.data['results']), 10)

    def test_get_urls_by_date(self):
        response = self.client.get('/urls/?from=2020-01-07T10:05:00&to=2020-01-08')
        objects = URLMapper.objects.filter(create__lte="2020-01-08", create__gte="2020-01-07")
        self.assertEqual(len(response.data), len(objects))
