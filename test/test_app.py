import unittest
from app import create_app

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

    def test_create_app(self):
        self.assertIsNotNone(self.app)

    def test_index_page(self):
        rv = self.client.get('/')
        self.assertEqual(rv.status_code, 200)
    
if __name__ == '__main__':
    unittest.main()