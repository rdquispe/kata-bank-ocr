import src.constants as constant


class KataParser(object):

    def parser(self, account_line):
        cells = self.get_cells(account_line)
        cell_values = []
        for cell in cells:
            cell_values.append(self.__get_cell_value(cell))

        return tuple(cell_values)

    def get_cells(self, account_line):
        cells = []

        lines = self.__get_lines(account_line)

        for offset in range(0, 26, 3):
            cell = lines[0][offset:offset + 3]
            cell += lines[1][offset:offset + 3]
            cell += lines[2][offset:offset + 3]
            cells.append(cell)

        return cells

    def __get_lines(self, account_line):
        lines = ["", "", ""]
        offset = 0

        for char in account_line:
            lines[offset] += char
            if len(lines[offset]) == 27:
                offset += 1

        return lines

    def __get_cell_value(self, cell):
        return constant.CELL_VALUES.get(cell, '?')

    def format_cell(self, cell):
        return str.format('{0}\n{1}\n{2}', cell[0:3], cell[3:6], cell[6:9])
