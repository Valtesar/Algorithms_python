from generator_lists import generator_lists
"""Сортировка элементов списка в порядке возрастания с использованием алгоритма сортировки гибридным методом"""


def heapify(numbers, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and numbers[largest] < numbers[left]:
        largest = left

    if right < n and numbers[largest] < numbers[right]:
        largest = right

    if largest != i:
        numbers[i], numbers[largest] = numbers[largest], numbers[i]

        heapify(numbers, n, largest)
