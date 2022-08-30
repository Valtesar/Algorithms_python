from instruments.generator_lists import full_random_generator_lists, reversed_generator_lists

"""Сортировка элементов списка в порядке возрастания с использованием алгоритма сортировки гибридным методом"""

MIN_MERGE = 32


def calc_min_run(n):
    r = 0
    while n >= MIN_MERGE:
        r |= n & 1
        n >>= 1
    return n + r


def insertion_sort(numbers, left, right):
    for i in range(left + 1, right + 1):
        j = i
        while j > left and numbers[j] < numbers[j - 1]:
            numbers[j], numbers[j - 1] = numbers[j - 1], numbers[j]
            j -= 1


def merge(numbers, left, middle, right):
    len1, len2 = middle - left + 1, right - middle
    left, right = [], []
    for i in range(0, len1):
        left.append(numbers[left + i])
    for i in range(0, len2):
        right.append(numbers[middle + 1 + i])

    i, j, k = 0, 0, left

    while i < len1 and j < len2:
        if left[i] <= right[j]:
            numbers[k] = left[i]
            i += 1

        else:
            numbers[k] = right[j]
            j += 1

        k += 1

    while i < len1:
        numbers[k] = left[i]
        k += 1
        i += 1

    while j < len2:
        numbers[k] = right[j]
        k += 1
        j += 1


def tim_sort(numbers):
    n = len(numbers)
    min_run = calc_min_run(n)

    for start in range(0, n, min_run):
        end = min(start + min_run - 1, n - 1)
        insertion_sort(numbers, start, end)

    size = min_run
    while size < n:

        for left in range(0, n, 2 * size):

            mid = min(n - 1, left + size - 1)
            right = min((left + 2 * size - 1), (n - 1))

            if mid < right:
                merge(numbers, left, mid, right)

        size = 2 * size

    return numbers


def tim_sort_test():
    print('--- Full random list sorting ---')
    test_value = full_random_generator_lists(5, 10)
    for mas in test_value:
        print(f'Original list is: {*mas,}\nSorted list is: {tim_sort(mas)}\n')

    print('--- Reversed range list sorting ---')
    test_value = reversed_generator_lists(1, 20)
    for mas in test_value:
        print(f'Original list is: {*mas,}\nSorted list is: {tim_sort(mas)}\n')


if __name__ == '__main__':
    tim_sort_test()
