from find_and_replace import find_and_replace
from hours_minutes_seconds import get_hours_minutes_seconds
from calculus import maximum, minimum, sum, prod, moda, avg, median
from password_generator import gen_pwd


def run(choice):
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
        t = [3, 7, 10, 4, 1, 9, 6, 2, 8, 5]
        t_2 = [1, 1, 1, 3, 3, 4, 5, 6, 7, 7, 7, 10, 10, 5, 5, 5, 5, 5, 5]
        print(f'Maximum of {t} is', maximum(t))
        print(f'Minimum of {t} is', minimum(t))
        print(f'Sum of the elements in {t} is', sum(t))
        print(f'Product of the elements in {t} is', prod(t))
        print(f'Most frequent element in {t_2} is', moda(t_2))
        print(f'Average of elements in {t} is', avg(t))
        print(f'Median of {sorted(t)} is', median(t))
    elif choice == 4:
        length = 5
        print(f'Generated password of length {length} ->', gen_pwd(length))
