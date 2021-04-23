import io
import sys
import unittest
from unittest.mock import mock_open, patch

from functions import easy_as_a_pie, rational_insanity, turn_up_the_heat, intentional_bullshit


class TestFunctions(unittest.TestCase):

    def test_easy_as_a_pie(self):
        new_out = io.StringIO()
        old_out = sys.stdout
        sys.stdout = new_out
        easy_as_a_pie(1, 2)
        sys.stdout = old_out
        self.assertEqual(new_out.getvalue().strip(), '3')

    @patch('functions.stdin.readline')
    def test_rational_insanity(self, mock_readline):
        mock_readline.return_value = 4
        self.assertEqual(rational_insanity(5), 9)

    @patch('functions.stdout.write')
    def test_turn_up_the_heat(self, write):
        turn_up_the_heat(10, 11)
        write.assert_called_once_with('21')

    def test_intentional_bullshit(self):
        with patch('functions.open', mock_open()) as output:
            intentional_bullshit(22, 23)
        output.return_value.write.assert_called_once_with('45')


if __name__ == '__main__':
    unittest.main()
