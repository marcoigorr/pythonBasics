
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


def mode(t) -> int:
    # Dictionary with frequencies of each element of t
    dCounts = {}
    _mode = 0

    # Loop through t
    for i in range(len(t)):
        # If the element is in dictionary add 1; else set it to 1
        if t[i] in dCounts:
            dCounts[t[i]] += 1
        else:
            dCounts[t[i]] = 1

    # Find the key with the highest value
    for key in dCounts.keys():
        # If current key value is the highest in the list of values then it's the mode
        if dCounts[key] == maximum(list(dCounts.values())):
            _mode = key

    return _mode


def avg(t) -> float:
    return sum(t) / len(t)


def median(t) -> int:
    t = sorted(t)

    # If odd; else if even
    if len(t) % 2 != 0:
        return t[(len(t)) // 2]
    else:
        return (t[(len(t) // 2) - 1] + t[(len(t) // 2)]) / 2
