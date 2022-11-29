import random
import string


def gen_pwd(length) -> str:
    special = '~!@#$%^&*()_+.'
    pwd = [None] * length

    if length < 8:
        length = 8

    # Get random chars
    for i in range(0, length):
        pwd[i] = random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits + special)

    # Mix chars
    for j in range(length):
        n1 = random.randint(0, length - 1)
        n2 = random.randint(0, length - 1)

        x = pwd[n1]
        pwd[n1] = pwd[n2]
        pwd[n2] = x

    # Cut string if pwd_length > length
    if len(pwd) > length:
        pwd = pwd[:8]

    return ''.join(pwd)
