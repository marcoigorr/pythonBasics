
def print_handshakes(people):
    handshakes = {}

    for i in range(len(people)):
        for j in range(i, len(people) - 1):
            if people[i] not in handshakes:
                handshakes[people[i]] = people[j + 1]
            else:
                handshakes[people[i]] += ',', people[j + 1]

    return len(handshakes.values())
