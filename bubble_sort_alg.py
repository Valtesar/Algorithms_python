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

def bubble_sort_test():
