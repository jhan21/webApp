
import unittest
from unittest.mock import patch, Mock
from flask import Flask
from app import main

class FlaskAppTests(unittest.TestCase):
    def setUp(self):
        # Create a test Flask app
        self.app = Flask(__name__)
        self.app.config['TESTING_MOCK'] = True

    @patch('app.requests.get')
    def test_main_route(self, mock_get):

        mock_response = Mock()
        mock_response.json.return_value = {'key': 'value'}
        mock_get.return_value = mock_response

        with self.app.test_client() as client:
            response = client.get('/')

        self.assertIn(b'key', response.data)
        self.assertIn(b'value', response.data)

if __name__ == '__main__':
    unittest.main()