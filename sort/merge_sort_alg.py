from instruments.generator_lists import full_random_generator_lists

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
    test_value = full_random_generator_lists(5, 10)
    for mas in test_value:
        print(f'Original list is: {*mas,}\nSorted list is: {merge_sort(mas)}\n')


if __name__ == '__main__':
    merge_sort_test()
