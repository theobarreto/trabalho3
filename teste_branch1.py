import unittest
from unittest.mock import patch
from password_checker import main

class TestBranch1(unittest.TestCase):
    @patch('builtins.input', side_effect=['path/to/your/testfile.txt'])
    def test_branch_1(self, mock_input):
        with patch('getpass.getpass', return_value='password123'):
            self.assertEqual(main(), 0)

if __name__ == '__main__':
    unittest.main()