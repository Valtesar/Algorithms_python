from instruments.generator_lists import full_random_generator_lists

"""Сортировка элементов списка в порядке возрастания с использованием алгоритма сортировки методом Шелла"""


def shell_sort(numbers):

    step = len(numbers) // 2

    while step > 0:

        for i in range(step, len(numbers)):
            temp = numbers[i]
            j = i

            while j >= step and numbers[j - step] > temp:
                numbers[j] = numbers[j - step]
                j -= step
                numbers[j] = temp

        step //= 2

    return numbers


def shell_sort_test():
    test_value = full_random_generator_lists(5, 10)
    for mas in test_value:
        print(f'Original list is: {*mas,}\nSorted list is: {shell_sort(mas)}\n')


if __name__ == '__main__':
    shell_sort_test()

