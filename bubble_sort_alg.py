from generator_lists import full_random_generator_lists
"""Сортировка элементов списка в порядке возрастания с использованием алгоритма сортировки 'пузырьком'"""


def bubble_sort(numbers: list) -> list:
    n = len(numbers)
    for i in range(n):
        numbers_sorted = True

        for j in range(n - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                numbers_sorted = False
        if numbers_sorted:
            return numbers


def bubble_sort_test():
    test_value = full_random_generator_lists(5, 10)
    for mas in test_value:
        print(f'Original list is: {*mas,}\nSorted list is: {bubble_sort(mas)}\n')


if __name__ == '__main__':
    bubble_sort_test()
