import unittest
from flask import Flask
from app import calculate_temperature_difference

class FlaskAppTests(unittest.TestCase):
    def setUp(self):
        # Create a test Flask app
        self.app = Flask(__name__)
        self.app.config['TESTING'] = True

    def test_calculate_temperature_difference(self):

        temperature1 = 20
        temperature2 = 15

        # Use the function
        result = calculate_temperature_difference(temperature1, temperature2)

        self.assertEqual(result, 5)

if __name__ == '__main__':
    unittest.main()
