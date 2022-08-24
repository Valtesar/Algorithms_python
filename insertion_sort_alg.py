import random
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


def generator_lists(count, length):
    """Создаем функцию генератор списков с параметрами:
        count - колличество списков,
        length - длинна списков"""
    start_num = 0
    end_num = 1000
    for i in range(count):
        arr = [random.randint(start_num, end_num) for _ in range(length)]
        yield arr
