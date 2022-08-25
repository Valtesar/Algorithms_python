from random import randint
from generator_lists import generator_lists

"""Сортировка элементов списка в порядке возрастания с использованием алгоритма сортировки методом слияния"""


def quicksort(numbers):

    if len(numbers) < 2:
        return numbers

    low, same, high = [], [], []

    pivot = numbers[randint(0, len(numbers) - 1)]

    for number in numbers:
        if number < pivot:
            low.append(number)
        elif number == pivot:
            same.append(number)
        elif number > pivot:
            high.append(number)

    return quicksort(low) + same + quicksort(high)


if __name__ == '__main__':
    print(quicksort([31, 23, 45, 100, 9, 34, 85, 72, 182]))
