import unittest
from src.parser import KataParser


class PhaseThreeTest(unittest.TestCase, KataParser):
    def test_ill_account_number(self):
        input = "    _  _  _  _  _  _     _ " \
                "|_||_|| || ||_   |  |  | _ " \
                "  | _||_||_||_|  |  |    _|"

        account_number = self.parser(input)
        self.assertTrue(account_number == ('4', '9', '0', '0', '6', '7', '7', '?', '?'))

    def test_account_number(self):
        input = " _  _  _  _  _  _  _  _  _ " \
                "| || || || || || || ||_ | |" \
                "|_||_||_||_||_||_||_| _||_|"

        account_number = self.parser(input)
        self.assertTrue(account_number == ('0', '0', '0', '0', '0', '0', '0', '5', '0'))


if __name__ == '__main__':
    unittest.main()
