class Checksum(object):
    def checksum(self, number_tuple):
        sum = 0
        factor = 1
        for digit in number_tuple[::-1]:
            if digit == '?':
                return False

            sum += factor * int(digit)
            factor += 1

        return (sum % 11) == 0
