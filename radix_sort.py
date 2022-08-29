from generator_lists import full_random_generator_lists
from generator_lists import reversed_generator_lists
"""Сортировка элементов списка в порядке возрастания с использованием алгоритма сортировки поразрядным методом"""


def counting_sort(numbers, exp1):
    n = len(numbers)
    output = [0] * n
    count = [0] * 10

    for i in range(0, n):
        index = numbers[i] // exp1
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1

    while i >= 0:
        index = numbers[i] // exp1
        output[count[index % 10] - 1] = numbers[i]
        count[index % 10] -= 1
        i -= 1

    i = 0
    for i in range(0, len(numbers)):
        numbers[i] = output[i]


def radix_sort(numbers):
    max_number = max(numbers)
    exp = 1
    while max_number / exp >= 1:
        counting_sort(numbers, exp)
        exp *= 10

    return numbers


def radix_sort_test():
    print('--- Full random list sorting ---')
    test_value = full_random_generator_lists(5, 10)
    for mas in test_value:
        print(f'Original list is: {*mas,}\nSorted list is: {radix_sort(mas)}\n')

    print('--- Reversed range list sorting ---')
    test_value = reversed_generator_lists(1, 20)
    for mas in test_value:
        print(f'Original list is: {*mas,}\nSorted list is: {radix_sort(mas)}\n')


if __name__ == '__main__':
    radix_sort_test()
