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


def heap_sort(numbers):
    n = len(numbers)

    for i in range(n // 2 - 1, -1, -1):
        heapify(numbers, n, i)

    for i in range(n - 1, 0, -1):
        numbers[i], numbers[0] = numbers[0], numbers[i]
        heapify(numbers, i, 0)
    return numbers


def heap_sort_test():
    test_value = generator_lists(5, 10)
    for mas in test_value:
        print(f'Original list is: {*mas,}\nSorted list is: {heap_sort(mas)}\n')


if __name__ == '__main__':
    heap_sort_test()
