from random import randint
from generator_lists import generator_lists

"""Сортировка элементов списка в порядке возрастания с использованием алгоритма сортировки методом слияния"""


def quick_sort(numbers):

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

    return quick_sort(low) + same + quick_sort(high)


def quick_sort_test():
    pass


if __name__ == '__main__':
    quick_sort_test()
