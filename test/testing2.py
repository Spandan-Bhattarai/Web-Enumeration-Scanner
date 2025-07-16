import io
import unittest
from unittest.mock import patch, MagicMock
from cli import SubdomainScanner, SubdirectoryScanner

class TestScanner(unittest.TestCase):
    @patch('builtins.input', side_effect=['geeksforgeeks.org', '1', 'test_output_subdomain.txt'])
    @patch('requests.get')
    @patch('builtins.open', create=True)
    def test_subdomain_scanner(self, mock_open, mock_requests_get, mock_input):
        scanner = SubdomainScanner()
        mock_open.return_value.__enter__.return_value.read.return_value = "www"
        mock_requests_get.side_effect = [MagicMock(status_code=200)] * 3

        scanner.scan('geeksforgeeks.org', '1')

        mock_requests_get.assert_called_with('https://www.geeksforgeeks.org')
        mock_open.assert_called_with('geeksforgeeks.org', 'w')
        mock_open.return_value.__enter__.return_value.write.assert_called_with("Target: https://www.geeksforgeeks.org\nStatus Code: 200\n\n")

    @patch('builtins.input', side_effect=['https://schoolworkspro.com/', '2', 'test_output_subdirectory.txt'])
    @patch('requests.get')
    @patch('builtins.open', create=True)
    def test_subdirectory_scanner(self, mock_open, mock_requests_get, mock_input):
        scanner = SubdirectoryScanner()
        mock_open.return_value.__enter__.return_value.read.return_value = "users"
        mock_requests_get.side_effect = [MagicMock(status_code=200)] * 3

        scanner.scan('https://schoolworkspro.com/', '2', 'test_output_subdirectory.txt')

        mock_requests_get.assert_called_with('https://schoolworkspro.com//users', verify=True)
        mock_open.assert_called_with('test_output_subdirectory.txt', 'w')
        mock_open.return_value.__enter__.return_value.write.assert_called_with("Target: https://schoolworkspro.com//users\nStatus Code: 200\n\n")

if __name__ == "__main__":
    unittest.main()
