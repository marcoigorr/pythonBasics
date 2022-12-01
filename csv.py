from find_and_replace import find_and_replace


class CsvStruct:
    n_lines = 0
    dictColumns = {}
    lRows = []
    row_matrix = []

    def __init__(self, file):
        self.file = file
        self.__init_dictionary__()
        self.__init_rows__()
        self.__init_matrix__()

    def __init_dictionary__(self):
        column = ''
        i = 0
        for char in self.file.readline():
            if char == ',':
                self.dictColumns[column] = i
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

    def to_string(self):
        print(self.dictColumns)


def is_float(element: any) -> bool:
    # If you expect None to be passed:
    if element is None:
        return False
    try:
        float(element)
        return True
    except ValueError:
        return False
