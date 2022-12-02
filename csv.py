from find_and_replace import find_and_replace


class Colors:
    def __init__(self):
        self.GREY = '\033[90m'
        self.RED = '\033[91m'
        self.GREEN = '\033[92m'
        self.DARK_GREEN = '\033[32m'
        self.YELLOW = '\033[93m'
        self.ORANGE = '\033[33m'
        self.BLUE = '\033[94m'
        self.MAGENTA = '\033[95m'
        self.CYAN = '\033[96m'
        self.WHITE = '\033[97m'

        self.END = '\033[0m'
        self.BOLD = '\033[1m'
        self.UNDERLINE = '\033[4m'

        self.list_colors = [
            self.ORANGE,
            self.RED,
            self.MAGENTA,
            self.DARK_GREEN,
            self.GREY,
            self.GREEN,
            self.CYAN,
            self.YELLOW,
            self.WHITE,
            self.MAGENTA,
            self.ORANGE,
            self.RED
        ]


class CsvStruct:
    n_lines = 0
    dictColumns = {}
    dictColumns_reversed = {}
    lRows = []
    row_matrix = []

    def __init__(self, file):
        self.file = file
        self.first_line = self.file.readline()
        self.__init_dictionary__(self.first_line)
        self.__init_dictionary__(self.first_line, reversed=True)
        self.__init_rows__()
        self.__init_matrix__()

    def __init_dictionary__(self, first_line, reversed=False):
        if not reversed:
            column = ''
            i = 0
            for char in first_line:
                if char == ',':
                    self.dictColumns[column] = i
                    i += 1
                    column = ''
                else:
                    column += char
        else:
            column = ''
            i = 0
            for char in first_line:
                if char == ',':
                    self.dictColumns_reversed[i] = column
                    i += 1
                    column = ''
                else:
                    column += char

    def __init_rows__(self):
        for row in self.file.readlines():
            self.lRows.append(find_and_replace(row, '\n', ''))
            self.n_lines += 1

    def __init_matrix__(self):
        for i in range(self.n_lines):
            self.row_matrix.append(self.__get_row_data__(i))

    def __get_row_data__(self, line):
        element_data = []
        data = ''
        comma_count = 0

        for char in self.lRows[line]:
            if char == ',':
                comma_count += 1  # 4
                if comma_count == 4:
                    data += char
                else:
                    if data != '':
                        # Check if data can be converted to int or float, if True cast data else don't cast
                        element_data.append(int(data) if data.isdigit() else float(data) if is_float(data) else data)
                    else:
                        element_data.append(None)

                    data = ''
            else:
                data += char

        element_data.append(data)  # final append for Embarked field

        return element_data

    def get_row_by_column_value(self, column, value):
        # Check instance of value in given column and returns the row
        for row in self.row_matrix:
            if row[self.dictColumns[column]] == value:
                return row

    def get_rows_by_column_value(self, column, value):
        list = []
        for row in self.row_matrix:
            if row[self.dictColumns[column]] == value:
                list.append(row)
        return list

    def __str__(self):
        c = Colors()
        str_columns = f'Columns: '

        for i in range(len(self.dictColumns_reversed)):
            str_columns += f"{c.list_colors[i]} {self.dictColumns_reversed[i]}"

        out_string = f'{str_columns} {c.END}\n'

        for row in self.row_matrix:
            length_row = len(row)
            strRow = ''
            for i in range(length_row):
                if i == length_row - 1:
                    strRow += f"{c.list_colors[i]} {row[i]}"
                else:
                    strRow += f"{c.list_colors[i]} {row[i]}{c.END},"
            out_string += f"{strRow} {c.END}\n"
        return out_string


def is_float(element: any) -> bool:
    # If you expect None to be passed:
    if element is None:
        return False
    try:
        float(element)
        return True
    except ValueError:
        return False
