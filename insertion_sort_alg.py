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
