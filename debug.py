from find_and_replace import find_and_replace
from hours_minutes_seconds import get_hours_minutes_seconds
from calculus import maximum, minimum, sum, prod, mode, avg, median
from password_generator import gen_pwd


def run(choice, assertion=False):
    if choice == 1:
        print(find_and_replace('The pen is on the table', 'pen', 'MADONNA'))
        print(find_and_replace('The pen is on the table', 'on', 'MARIO'))
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