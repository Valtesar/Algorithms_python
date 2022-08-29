from generator_lists import full_random_generator_lists
"""Сортировка элементов списка в порядке возрастания с использованием алгоритма сортировки методом вставки"""


def insertion_sort(numbers: list) -> list:
    for i in range(1, len(numbers)):
        key_item = numbers[i]
        j = i - 1
        while j >= 0 and numbers[j] > key_item:
            numbers[j + 1] = numbers[j]
            j -= 1
        numbers[j + 1] = key_item
    return numbers


def insertion_sort_test():
    test_value = full_random_generator_lists(5, 10)
    for mas in test_value:
        print(f'Original list is: {*mas,}\nSorted list is: {insertion_sort(mas)}\n')


if __name__ == '__main__':
    insertion_sort_test()
