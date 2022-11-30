import debug


def main() -> int:
    print('Available programs: \n')
    print('1) find and replace')
    print('2) hours, minutes, seconds')
    print('3) calculus')
    print('4) password generator')
    print('5) bubble sort')
    print('0) Exit')
    try:
        choice = int(input('\nYour choice -> '))
    except ValueError as e:
        print('Error:', e)
        return 1

    if 0 >= choice > 4:
        return 1

    debug.run(choice)

    return 0


if __name__ == '__main__':
    main()
