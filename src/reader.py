import src.constants as const
import exception.error as custom_exception


class KataReader(object):

    def read(self, filename):
        accounts = []
        number_line = ''
        row = 0
        try:
            with open(filename, const.READ) as file:
                for line in file:
                    row += 1

                    if row % 4 == 0:
                        accounts.append(number_line)
                        number_line = ''
                    else:
                        number_line += line.rstrip('\n')
        except Exception as e:
            custom_exception.logger.error(e)

        return accounts
