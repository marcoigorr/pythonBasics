from find_and_replace import find_and_replace


def is_float(element: any) -> bool:
    # If you expect None to be passed:
    if element is None:
        return False
    try:
        float(element)
        return True
    except ValueError:
        return False


class Colors:
    GREY = '\033[90m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    DARK_GREEN = '\033[32m'
    YELLOW = '\033[93m'
    ORANGE = '\033[33m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'

    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    list_colors = [ORANGE, RED, MAGENTA, DARK_GREEN, GREY, GREEN, CYAN, YELLOW, WHITE, MAGENTA, ORANGE, RED ]


class CsvStruct:
    def __init__(self, file):
        self.file = file
        self.c = Colors()
        self.n_lines = 0
        self.dictColumns = {}
        self.dictColumns_reversed = {}
        self.row_matrix = []

        self.list_people: Person = []

        self.__init_dictionaries__()
        self.__init_row_matrix__()
        self.__init_Person_list__()

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
                    # Count = 4 means that we are inside the name string which contains a comma to add
                    if comma_count == 4:
                        element += char
                    else:
                        # If the field is empty add None
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

    def __init_Person_list__(self):
        for row in self.row_matrix:
            person = Person(row, self.dictColumns_reversed)
            self.list_people.append(person)

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
        # Add Columns name
        str_columns = f'Columns: '
        for i in range(len(self.dictColumns_reversed)):
            str_columns += f"{self.c.list_colors[i]} {self.dictColumns_reversed[i]}"

        out_string = f'{str_columns} {self.c.END}\n'

        # Add all the rows
        for row in self.row_matrix:
            length_row = len(row)
            strRow = ''
            for i in range(length_row):
                if i == length_row - 1:
                    strRow += f"{self.c.list_colors[i]} {row[i]}"
                else:
                    strRow += f"{self.c.list_colors[i]} {row[i]}{self.c.END},"
            out_string += f"{strRow} {self.c.END}\n"
        return out_string

class Person():
    def __init__(self, row, dictColumns):
        self.row = row
        self.dictColumns = dictColumns

        self.PassengerId = row[0]
        self.Survived = row[1]
        self.Pclass = row[2]
        self.Name = row[3]
        self.Sex = row[4]
        self.Age = row[5]
        self.SibSp = row[6]
        self.Parch = row[7]
        self.Ticket = row[8]
        self.Fare = row[9]
        self.Cabin = row[10]
        self.Embarked = row[11]

    def __str__(self):
        out_string = f'PassengerId: {self.PassengerId}' \
                     f'Survived: {self.Survived}' \
                     f'Pclass: {self.Pclass}' \
                     f'Name: {self.Row}' \
                     f'Sex: {self.Sex}' \
                     f'Age: {self.Age}' \
                     f'SibSp: {self.SibSp}' \
                     f'Parch: {self.Parch}' \
                     f'Ticket: {self.Ticket}' \
                     f'Fare: {self.Fare}' \
                     f'Cabin: {self.Cabin}' \
                     f'Embarked: {self.Embarked}' \

        return out_string
