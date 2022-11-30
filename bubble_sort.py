
def bubble_sort(numbers):
    length: int = len(numbers)
    swapping: bool = True

    while swapping:
        swapping = False

        for i in range(length - 1):
            if numbers[i] > numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                swapping = True

    return numbers
