import random
import string


def gen_pwd(length) -> str:
    if length < 8:
        length = 8

    special = '~!@#$%^&*()_+.'

    pwd = [''] * length

    pwd[0] = random.choice(string.ascii_lowercase)
    pwd[1] = random.choice(string.ascii_uppercase)
    pwd[2] = random.choice(string.digits)
    pwd[3] = random.choice(special)

    # Get random chars
    random_chars = random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits + special, k=30)
    for i in range(4, length):
        pwd[i] = random.choice(random_chars)

    # Mix chars (optional)
    for j in range(length):
        n1 = random.randint(0, length - 1)
        n2 = random.randint(0, length - 1)

        pwd[n1], pwd[n2] = pwd[n2], pwd[n1]

    return ''.join(pwd)
