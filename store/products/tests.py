from django.test import TestCase

class TestIndex(TestCase):
    def test_index(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context_data['title'], 'Главная')
