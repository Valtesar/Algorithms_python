from random import randint
from generator_lists import generator_lists

"""Сортировка элементов списка в порядке возрастания с использованием алгоритма сортировки методом быстрой сортировки"""


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
    test_value = generator_lists(5, 10)
    for mas in test_value:
        print(f'Original list is: {*mas,}\nSorted list is: {quick_sort(mas)}\n')


if __name__ == '__main__':
    quick_sort_test()
