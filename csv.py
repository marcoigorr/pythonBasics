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
    c = Colors()
    n_lines = 0
    dictColumns = {}
    dictColumns_reversed = {}
    row_matrix = []

    def __init__(self, file):
        self.file = file
        self.__init_dictionaries__()
        self.__init_row_matrix__()

    def __init_dictionaries__(self):
        column = ''
        i = 0
        for char in self.file.readline():
            if char == ',' or char == '\n':
                self.dictColumns[column] = i
                self.dictColumns_reversed[i] = column
                i += 1
                column = ''
            else:
                column += char

    def __init_row_matrix__(self):
        for row in self.file.readlines():
            self.n_lines += 1
            row = find_and_replace(row, '\n', '')

            row_elements = []
            element = ''
            comma_count = 0
            for char in row:
                if char == ',':
                    comma_count += 1  # 4
                    if comma_count == 4:
                        element += char
                    else:
                        if element != '':
                            # Check if data can be converted to int or float, if True cast data else don't cast
                            row_elements.append(int(element) if element.isdigit() else float(element) if is_float(element) else element)
                        else:
                            row_elements.append(None)

                        element = ''
                else:
                    element += char

            row_elements.append(element)  # final append for Embarked field

            self.row_matrix.append(row_elements)

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
        return self.__to_string__(list)

    def __to_string__(self, matrix=None):
        if matrix is None:
            matrix = self.row_matrix

        # Add Columns name
        str_columns = f'Columns: '
        for i in range(len(self.dictColumns_reversed)):
            str_columns += f"{self.c.list_colors[i]} {self.dictColumns_reversed[i]}"

        out_string = f'{str_columns} {self.c.END}\n'

        # Add all the rows
        for row in matrix:
            length_row = len(row)
            strRow = ''
            for i in range(length_row):
                if i == length_row - 1:
                    strRow += f"{self.c.list_colors[i]} {row[i]}"
                else:
                    strRow += f"{self.c.list_colors[i]} {row[i]}{self.c.END},"
            out_string += f"{strRow} {self.c.END}\n"
        return out_string

    def __str__(self):
        return self.__to_string__()


def is_float(element: any) -> bool:
    # If you expect None to be passed:
    if element is None:
        return False
    try:
        float(element)
        return True
    except ValueError:
        return False
