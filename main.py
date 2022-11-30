from find_and_replace import find_and_replace
from hours_minutes_seconds import get_hours_minutes_seconds
import calculus
from password_generator import gen_pwd


def main() -> int:
    print('Available programs: \n')
    print('1) find and replace')
    print('2) hours, minutes, seconds')
    print('3) calculus')
    print('4) password generator')
    print('0) Exit')
    choice = int(input('\nYour choice -> '))

    if choice == 0:
        return 1
    elif choice == 1:
        # assert find_and_replace('The fox', 'fox', 'do') == 'The dog', 'Failed find_and_replace()'
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
        print(f'Maximum of {t} is', calculus.maximum(t))
        print(f'Minimum of {t} is', calculus.minimum(t))
        print(f'Sum of the elements in {t} is', calculus.sum(t))
        print(f'Product of the elements in {t} is', calculus.prod(t))
        print(f'Most frequent element in {t} is', calculus.moda(t))
        print(f'Average of elements in {t} is', calculus.avg(t))
        print(f'Median of {sorted(t)} is', calculus.median(t))
    elif choice == 4:
        print('Generated password ->', gen_pwd(16))

    return 0


if __name__ == '__main__':
    main()
