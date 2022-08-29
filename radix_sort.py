from generator_lists import generator_lists

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

