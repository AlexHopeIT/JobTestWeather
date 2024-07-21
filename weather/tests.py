import unittest
from unittest.mock import patch, Mock
from api_client import get_weather


class TestGetWeather(unittest.TestCase):

    @patch('my_module.requests.get')
    def test_get_weather_success(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'main': {'temp': 25},
            'weather': [{'description': 'Clear sky'}]
        }
        mock_get.return_value = mock_response

        result = get_weather('London')
        self.assertEqual(result['city'], 'London')
        self.assertEqual(result['temperature'], 25)
        self.assertEqual(result['description'], 'Clear sky')

    @patch('my_module.requests.get')
    def test_get_weather_failure(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response

        result = get_weather('NotFoundCity')
        self.assertIsNone(result)


if __name__ == '__main__':
    unittest.main()
