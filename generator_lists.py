import random
"""Функция генерации списков с параметрами: count - колличество списков, length - длинна списков.
   Возвращает генератор списков"""


def generator_lists(count, length):
    """Создаем функцию генератор списков с параметрами:
        count - колличество списков,
        length - длинна списков"""
    start_num = 0
    end_num = 1000
    for i in range(count):
        arr = [random.randint(start_num, end_num) for _ in range(length)]
        yield arr
