from merge_sort_alg import merge

"""Сортировка элементов списка в порядке возрастания с использованием алгоритма сортировки гибридным методом"""


def insertion_sort(numbers, left=0, right=None):
    if right is None:
        right = len(numbers) - 1

    for i in range(left + 1, right + 1):
        key_item = numbers[i]
        j = i - 1

        while j >= left and numbers[i] > key_item:
            numbers[j + 1] = numbers[j]
            j -= 1

        numbers[j + 1] = key_item

    return numbers


def tim_sort(numbers):
    min_run = 32
    n = len(numbers)
    for i in range(0, n, min_run):
        insertion_sort(numbers, i, min((i + min_run - 1), n - 1))

    size = min_run
    while size < n:
        for start in range(0, n, size * 2):
            midpoint = start + size - 1
            end = min((start + size * 2 - 1), (n - 1))
            merged_numbers = merge(
                left=numbers[start:midpoint + 1],
                right=numbers[midpoint + 1:end + 1])
            numbers[start:start+len(merged_numbers)] = merged_numbers

        size *= 2

    return numbers

