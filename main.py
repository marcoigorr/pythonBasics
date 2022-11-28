from find_and_replace import find_and_replace
from hours_minutes_seconds import  get_hours_minutes_seconds


def main():
    print('Available programs: \n')
    print('1) find and replace')
    print('2) hours, minutes, seconds')
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


if __name__ == '__main__':
    main()
