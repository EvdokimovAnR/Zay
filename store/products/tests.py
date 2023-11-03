from django.test import TestCase
from store.wsgi import *
from http import HTTPStatus

class TestIndex(TestCase):
    def test_index(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertIn('Главная', response.content.decode())
        # self.assertTemplateUsed(response, 'products/index.html')


