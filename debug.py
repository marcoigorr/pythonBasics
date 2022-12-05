from find_and_replace import find_and_replace
from hours_minutes_seconds import get_hours_minutes_seconds
from calculus import maximum, minimum, sum, prod, mode, avg, median
from password_generator import gen_pwd
from bubble_sort import bubble_sort
from handshakes import print_handshakes
from random_shuffle import shuffle
from merge_list import merge_lists
from csv import CsvStruct


def run(choice):
    if choice == 1:
        print("find_and_replace('The fox', 'fox', 'dog') == 'The dog' ? ", find_and_replace('The fox', 'fox', 'dog') == 'The dog')
        print("find_and_replace('fox', 'fox', 'dog') == 'dog' ? ", find_and_replace('fox', 'fox', 'dog') == 'dog')
        print("find_and_replace('Firefox', 'fox', 'dog') == 'Firedog' ? ", find_and_replace('Firefox', 'fox', 'dog') == 'Firedog')
        print("find_and_replace('foxfox', 'fox', 'dog') == 'dogdog' ? ", find_and_replace('foxfox', 'fox', 'dog') == 'dogdog')
        print("find_and_replace('The Fox and fox.', 'fox', 'dog') == 'The Fox and dog.' ? ", find_and_replace('The Fox and fox.', 'fox', 'dog') == 'The Fox and dog.')
        print("find_and_replace('THE FOX AND THE DOG' 'fox', 'dog') == 'THE FOX AND THE DOG' ? ", find_and_replace('THE FOX AND THE DOG', 'fox', 'dog') == 'THE FOX AND THE DOG')

    elif choice == 2:
        print(get_hours_minutes_seconds(30))
        print(get_hours_minutes_seconds(60))
        print(get_hours_minutes_seconds(90))
        print(get_hours_minutes_seconds(3600))
        print(get_hours_minutes_seconds(3601))
        print(get_hours_minutes_seconds(3661))
        print(get_hours_minutes_seconds(90042))
        print(get_hours_minutes_seconds(91842))
        print(get_hours_minutes_seconds(0))

    elif choice == 3:
        t = [1, 2, 3, 4, 5, 7]
        print(f't = {t}')
        print('maximum(t) == 7 ?', maximum(t) == 7)
        print('minimum(t) == 1 ?', minimum(t) == 1)
        print('sum(t) == 22 ?', sum(t) == 22)
        print('prod(t) == 840', prod(t) == 840)
        print('round(avg(t), 2) == 3.67 ?', round(avg(t), 2) == 3.67)
        print('median(t) == 3.5 ?', median(t) == 3.5)
        print('moda([1, 2, 3, 1, 2, 1, 1, 1, 2]) == 1 ?', mode([1, 2, 3, 1, 2, 1, 1, 1, 2]) == 1)
        print('moda([1, 2, 3, 3, 3, 1, 2, 1, 2, 3, 3, 3]) == 3 ?', mode([1, 2, 3, 3, 3, 1, 2, 1, 2, 3, 3, 3]) == 3)

        import random
        random.seed(42)
        t_2 = [3, 7, 10, 4, 1, 9, 6, 2, 8]
        for _ in range(5):
            random.shuffle(t_2)
            print(f't = {t_2}')
            print('median(t) == 6 ? ', median(t_2) == 6)

    elif choice == 4:
        print('len(gen_pwd(7)) == 8 ', len(gen_pwd(7)) == 8)
        print('len(gen_pwd(8)) == 8 ', len(gen_pwd(8)) == 8)
        from string import ascii_uppercase, ascii_lowercase, digits
        special = '~!@#$%^&*()_+.'
        pwd = gen_pwd(8)
        print(f'password = {pwd}')
        print('ascii_uppercase char? ', any(c in pwd for c in ascii_uppercase))
        print('ascii_lowercase char? ', any(c in pwd for c in ascii_lowercase))
        print('digits char? ', any(d in pwd for d in digits))
        print('special char? ', any(s in pwd for s in special))

    elif choice == 5:
        print('bubble_sort([2, 0, 4, 1, 3]) == [0, 1, 2, 3, 4] ? ', bubble_sort([2, 0, 4, 1, 3]) == [0, 1, 2, 3, 4])
        print('bubble_sort([2, 2, 2, 2]) == [2, 2, 2, 2] ? ', bubble_sort([2, 2, 2, 2]) == [2, 2, 2, 2])

    elif choice == 6:
        assert print_handshakes(['Alice', 'Bob']) == 1
        assert print_handshakes(['Alice', 'Bob', 'Carol']) == 3
        assert print_handshakes(['Alice', 'Bob', 'Carol', 'David']) == 6

    elif choice == 7:
        import random
        random.seed(42)
        # Perform this test ten times:
        for i in range(10):
            testData1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            shuffle(testData1)
        # Make sure the number of values hasn't changed:
        assert len(testData1) == 10
        # Make sure the order has changed:
        assert testData1 != [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        # Make sure that when re-sorted, all the original values are there:
        assert sorted(testData1) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        # Make sure an empty list shuffled remains empty:
        testData2 = []
        shuffle(testData2)
        assert testData2 == []

    elif choice == 8:
        assert merge_lists([1, 3, 6], [5, 7, 8, 9]) == [1, 3, 5, 6, 7, 8, 9]
        assert merge_lists([1, 2, 3], [4, 5]) == [1, 2, 3, 4, 5]
        assert merge_lists([4, 5], [1, 2, 3]) == [1, 2, 3, 4, 5]
        assert merge_lists([2, 2, 2], [2, 2, 2]) == [2, 2, 2, 2, 2, 2]
        assert merge_lists([1, 2, 3], []) == [1, 2, 3]
        assert merge_lists([], [1, 2, 3]) == [1, 2, 3]

    elif choice == 9:
        with open("titanic.csv") as file:
            Titanic = CsvStruct(file)
            print(Titanic)

            print(Titanic.get_rows_by_column_value('PassengerId', 1))
            print(Titanic.get_rows_by_column_value('Survived', 1))

        file.close()

    else:
        print('Quitting...')
