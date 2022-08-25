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


if __name__ == '__main__':
    print(shell_sort([93, 23, 56, 123, 563, 2, 124, 553, 423, 1245]))

