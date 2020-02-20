import unittest
from src.parser import KataParser
from src.checksum import Checksum


class PhaseTwoTest(unittest.TestCase, KataParser, Checksum):
    def test_valid_checksum(self):
        input = " _  _  _  _  _  _  _  _  _ " \
                "| || ||_|| || || || ||_ | |" \
                "|_||_||_||_||_||_||_| _||_|"

        account_number = self.parser(input)
        check = self.checksum(account_number)
        self.assertTrue(check)

    def test_invalid_checksum(self):
        input = "                           " \
                "  |  |  |  |  |  |  |  |  |" \
                "  |  |  |  |  |  |  |  |  |"

        account_number = self.parser(input)
        check = self.checksum(account_number)
        self.assertFalse(check)


if __name__ == '__main__':
    unittest.main()
