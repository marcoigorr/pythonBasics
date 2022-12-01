
def print_handshakes(people) -> int:
    length = len(people)
    nHandshakes = 0
    strHandshakes = ''

    for i in range(length - 1):
        for j in range(i + 1, length):
            nHandshakes += 1
            strHandshakes += f"\n{people[i]} shakes hand with {people[j]}"

    print(f"Handshakes: {strHandshakes} \nCount: {nHandshakes}\n")

    return nHandshakes
