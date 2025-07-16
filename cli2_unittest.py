import unittest
from unittest.mock import patch, mock_open
from final_cli import WordlistGenerator, SubdomainScanner, SubdirectoryScanner

class TestWordlistGenerator(unittest.TestCase):
    @patch('builtins.input', side_effect=['1', 'test.txt'])
    @patch('requests.get')
    @patch('builtins.open', new_callable=mock_open)
    def test_generate_wordlist(self, mock_open, mock_requests_get, mock_input):
        generator = WordlistGenerator()
        generator.generate_wordlist()

        mock_requests_get.assert_called_once_with('https://raw.githubusercontent.com/danTaler/WordLists/master/Subdomain.txt')
        mock_open.assert_called_once_with('test.txt', 'wb')
        mock_open().write.assert_called_once()

class TestSubdomainScanner(unittest.TestCase):
    @patch('builtins.input', side_effect=['test.com', 'test.txt'])
    @patch('requests.get')
    @patch('builtins.open', new_callable=mock_open)
    def test_scan(self, mock_open, mock_requests_get, mock_input):
        scanner = SubdomainScanner()
        scanner.scan('test.com', 'test.txt')

        mock_open.assert_called_once_with('test.txt', 'r')
        mock_requests_get.assert_called_once()
        mock_open().write.assert_called_once()

class TestSubdirectoryScanner(unittest.TestCase):
    @patch('builtins.input', side_effect=['test.com', 'test.txt', 'output.txt'])
    @patch('requests.get')
    @patch('builtins.open', new_callable=mock_open)
    def test_scan(self, mock_open, mock_requests_get, mock_input):
        scanner = SubdirectoryScanner()
        scanner.scan('test.com', 'test.txt', 'output.txt')

        mock_open.assert_called_with('test.txt', 'r')
        mock_requests_get.assert_called()
        mock_open().write.assert_called()

if __name__ == '__main__':
    unittest.main()
