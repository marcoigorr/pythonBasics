import random


def shuffle(values):
    length = len(values)

    random.seed(random.randint(0, 999))

    for i in range(length):
        n1 = random.randint(0, length - 1)
        n2 = random.randint(0, length - 1)

        values[n1], values[n2] = values[n2], values[n1]

    return values
