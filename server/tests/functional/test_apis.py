from ..conftest import BaseTestCase

class ApisTestCase(BaseTestCase):
    def test_categories(self):
        response = self.client.get('/categories/')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, list)