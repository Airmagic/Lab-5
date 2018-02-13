import unittest
from unittest.mock import patch
import MockInputRPS

class TestRPS(unittest.TestCase):
    @patch('builtins.input', return_value='1')
    def test_rock_scissors(self, mock_input):
        self.assertEqual(1,main())
