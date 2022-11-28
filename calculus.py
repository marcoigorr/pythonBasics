
def maximum(t) -> int:
    max = t[0]

    for i in range(len(t) - 1):
        if max < t[i + 1]:
            max = t[i + 1]

    return max


def minimum(t) -> int:
    min = t[0]

    for i in range(len(t) - 1):
        if min > t[i + 1]:
            min = t[i + 1]

    return min


def sum(t) -> int:
    sum = 0

    for i in range(len(t)):
        sum += t[i]

    return sum


def prod(t) -> int:
    prod = 1

    for i in range(len(t)):
        prod *= t[i]

    return prod


def moda(t) -> int:
    highest_count: int = 0

    for i in range(len(t)):
        element = t[i]

        current_count = 0
        for j in range(len(t)):
            if t[j] == element:
                current_count += 1

        if current_count > highest_count:
            highest_count = current_count
            moda = element

    return moda


def avg(t):
    pass


def median(t):
    pass
