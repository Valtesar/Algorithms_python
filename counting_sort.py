from generator_lists import full_random_generator_lists
from generator_lists import reversed_generator_lists

"""Сортировка элементов списка в порядке возрастания с использованием алгоритма сортировки методом подсчета"""


def counting_sort(numbers):
    max_number = int(max(numbers))
    min_number = int(min(numbers))
    range_of_numbers = max_number - min_number + 1
    count_numbers = [0 for _ in range(range_of_numbers)]
    output_numbers = [0 for _ in range(len(numbers))]

    for i in range(0, len(numbers)):
        count_numbers[numbers[i] - min_number] += 1

    for i in range(1, len(count_numbers)):
        count_numbers[i] += count_numbers[i - 1]

    for i in range(len(numbers) - 1, -1, -1):
        output_numbers[count_numbers[numbers[i] - min_number] - 1] = numbers[i]
        count_numbers[numbers[i] - min_number] -= 1

    for i in range(0, len(numbers)):
        numbers[i] = output_numbers[i]

    return numbers
