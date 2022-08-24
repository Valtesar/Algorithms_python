from generator_lists import generator_lists
"""Сортировка элементов списка в порядке возрастания с использованием алгоритма сортировки методом слияния"""


def merge(left, right):

    if len(left) == 0:
        return right

    if len(right) == 0:
        return left

    result = []
    index_left = index_right = 0

    while len(result) < len(left) + len(right):

        if left[index_left] <= right[index_right]:
            result.append(left[index_left])
            index_left += 1
        else:
            result.append(right[index_right])
            index_right += 1

        if index_right == len(right):
            result += left[index_left:]
            break

        if index_left == len(left):
            result += right[index_right:]
            break

    return result


def merge_sort(numbers):
    if len(numbers) < 2:
        return numbers

    midpoint = len(numbers) // 2

    return merge(
        left=merge_sort(numbers[:midpoint]),
        right=merge_sort(numbers[midpoint:]))


def merge_sort_test():
    pass


if __name__ == '__main__':
    merge_sort_test()
    print(merge_sort([9, 111, 43, 64, 21, 75, 554, 24, 0, 12, 10]))