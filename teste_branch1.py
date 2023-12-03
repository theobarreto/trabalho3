import unittest
from unittest.mock import patch
from password_checker import main

class TestBranch1(unittest.TestCase):
    def test_branch_1(self):
        # Substitua 'caminho/para/sua/testfile.txt' pelo caminho real fornecido no github actions
        user_file_path = 'path/to/your/testfile.txt'

        with patch('builtins.input', return_value=user_file_path):
            with patch('getpass.getpass', return_value='password123'):
                self.assertEqual(main(), 0)

if __name__ == '__main__':
    unittest.main()
