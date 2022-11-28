from find_and_replace import find_and_replace
from hours_minutes_seconds import get_hours_minutes_seconds
import calculus


def main():
    print('Available programs: \n')
    print('1) find and replace')
    print('2) hours, minutes, seconds')
    print('3) calculus')
    choice = int(input('\nYour choice -> '))

    if choice == 1:
        assert find_and_replace('The fox', 'fox', 'dog') == 'The dog', 'Failed find_and_replace()'
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
        t = [1, 2, 3, 12, 12, 7, 1, 1, 1, 1, 1]
        print(f'Maximum of {t} is', calculus.maximum(t))
        print(f'Minimum of {t} is', calculus.minimum(t))
        print(f'Sum of the elements in {t} is', calculus.sum(t))
        print(f'Product of the elements in {t} is', calculus.prod(t))
        print(f'Most frequent element of {t} is', calculus.moda(t))


if __name__ == '__main__':
    main()
