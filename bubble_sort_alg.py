import random
"""Сортировка элементов списка в порядке возрастания с использованием алгоритмы сортировки 'пузырьком'"""


def bubble_sort(numbers: list) -> list:
    flag = True
    while flag:
        flag = False
        for i in range(len(numbers) - 1):
            if numbers[i] > numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                flag = True
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
