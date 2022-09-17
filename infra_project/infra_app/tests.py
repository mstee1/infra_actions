from http import HTTPStatus

from django.test import Client, TestCase


class StaticPagesURLTests(TestCase):
    def setUp(self):
        self.guest_client = Client()

    def test_about_url_exists_at_desired_location(self):
        """Проверка доступности страниц."""
        response = self.guest_client.get('http://127.0.0.1:8000')
        self.assertEqual(response.status_code, HTTPStatus.OK)

        response = self.guest_client.get('http://127.0.0.1:8000/second/')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_page_shows_correct_content(self):
        """Проверка контента страниц."""
        response = self.guest_client.get('http://127.0.0.1:8000')
        self.assertContains(response, 'У меня получилось!')

        response = self.guest_client.get('http://127.0.0.1:8000/second/')
        self.assertContains(response, 'А это вторая страница!')
