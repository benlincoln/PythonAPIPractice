import unittest

from app import app


class MyTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_hw(self):
        response = self.app.get('/')
        self.assertEqual(response.data, b'Hello World!')

    def test_hn(self):
        response = self.app.get('/dog')
        self.assertEqual(response.data, b'Hello dog!')

    def test_json(self):
        response = self.app.get('/json')
        self.assertEqual(response.data, b'{"return": "fish"}')


if __name__ == '__main__':
    unittest.main()
