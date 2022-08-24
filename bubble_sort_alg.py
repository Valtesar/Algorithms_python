import random
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


def generator_lists(count, length):
    """Создаем функцию генератор списков с параметрами:
        count - колличество списков,
        length - длинна списков"""
    start_num = 0
    end_num = 1000
    for i in range(count):
        arr = [random.randint(start_num, end_num) for _ in range(length)]
        yield arr


def bubble_sort_test():
    test_value = generator_lists(5, 10)
    for mas in test_value:
        print(f'Original list is: {*mas,}\nSorted list is: {bubble_sort(mas)}\n')


if __name__ == '__main__':
    bubble_sort_test()
