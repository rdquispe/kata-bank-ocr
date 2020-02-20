from src.reader import KataReader
from src.parser import KataParser
from src.checksum import Checksum
import src.constants as constants


class Manager(object):
    __reader = KataReader()
    __parser = KataParser()
    __checksum = Checksum()

    def main_manager(self, filename):
        accounts = self.__reader.read(filename)

        for account in accounts:
            account_parser = self.__parser.parser(account)
            unrecognized_digits_index = self.__unrecognized_digits_index(account_parser)
            if len(unrecognized_digits_index) == 0:
                recovery_candidates = self.__recover_error(account_parser)
                print(self.__mark_amb_or_err(recovery_candidates, self.__tuple_to_string(account_parser)))
            elif len(unrecognized_digits_index) == 1:
                unrecognized_digit_index = unrecognized_digits_index[0]
                alternatives = self.__find_alternatives(account, unrecognized_digit_index)
                recovery_candidates = self.__recover_unreadable(self.__tuple_to_string(account_parser),
                                                                unrecognized_digit_index,
                                                                alternatives)
                print(self.__mark_amb_or_err(recovery_candidates, self.__tuple_to_string(account_parser)))
            else:
                print(self.__tuple_to_string(account_parser) + " ILL")

    def __recover_unreadable(self, candidate, position, alternatives):
        results = []
        for character in alternatives:
            validate_account = tuple(candidate[0:position]) + tuple(str(character)) + tuple(candidate[position + 1: len(candidate)])
            if self.__checksum.checksum(validate_account):
                results.append(validate_account)
        return results

    def __unrecognized_digits_index(self, account):
        index = 0
        index_unrecognized = []
        while index < len(account):
            if account[index] == '?':
                index_unrecognized.append(index)
            index += 1

        return index_unrecognized

    def __recover_error(self, account):
        results = []
        position = 0
        length = len(account)

        while position < length:
            alternative_digits = constants.ALTERNATIVES.get(account[position])
            for digit in alternative_digits:
                validate_account = tuple(account[0:position]) + tuple(str(digit)) + tuple(account[position + 1: length])
                if self.__checksum.checksum(validate_account):
                    results.append(validate_account)
            position += 1

        return results

    def __mark_amb_or_err(self, candidates, actual_result):
        if len(candidates) == 0:
            actual_result += " ERR"
        elif len(candidates) > 1:
            actual_result += " AMB"
        else:
            actual_result = self.__tuple_to_string(candidates[0])

        return actual_result

    def __tuple_to_string(self, input_tuple):
        return ''.join(input_tuple)

    def __find_alternatives(self, number_line, unrecognized_digit_index):
        one_symbol = self.__extract_one_symbol(number_line, unrecognized_digit_index * 3)
        alternatives = self.__decode_one_digit(one_symbol, constants.ILLEGAL_SYMBOLS)
        return constants.POSIBLE_DIGIT.get(alternatives)

    def __decode_one_digit(self, one_digit, illegal_symbols):
        position = 0
        while position < len(illegal_symbols[0]):
            match_count = 0
            for i in range(3):
                scan_line = one_digit[i]
                symbol_line = illegal_symbols[i][position:position + 3]
                if scan_line == symbol_line:
                    match_count += 1
            if match_count == 3:
                break
            position += 3
        if position >= len(illegal_symbols[0]):
            return '???'

        return illegal_symbols[3][position: position + 3]

    def __extract_one_symbol(self, number_line, position):
        lines = ["", "", ""]
        offset = 0

        for char in number_line:
            lines[offset] += char
            if len(lines[offset]) == 27:
                offset += 1

        result = [lines[0][position:position + 3],
                  lines[1][position:position + 3],
                  lines[2][position:position + 3]]

        return result
