from find_and_replace import find_and_replace


class CsvStruct:
    dColumns = {}
    lRows = []

    def __init__(self, file):
        self.file = file
        self.__init_columns__()
        self.__init_rows__()

    def __init_columns__(self):
        column = ''
        i = 0
        for char in self.file.readline():
            if char == ',':
                self.dColumns[i] = column
                i += 1
                column = ''
            else:
                column += char

    def __init_rows__(self):
        for row in self.file.readlines():
            self.lRows.append(find_and_replace(row, '\n', ''))

    def get_row_data(self, line):
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
                        element_data.append(data)
                    else:
                        element_data.append(None)

                    data = ''
            else:
                data += char

        element_data.append(data)  # final append for Embarked field

        return element_data

    def to_string(self):
        print(self.dColumns)
        print(self.lRows)


class Element:
    elementData = []
    dFields = {}

    def __init__(self, csvObject):
        self.csvObject = csvObject

    def get_row_data(self, line):
        pass
