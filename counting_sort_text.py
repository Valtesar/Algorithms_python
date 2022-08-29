"""Сортировка элементов списка в порядке возрастания с использованием алгоритма сортировки методом подсчета"""


def counting_sort(numbers):
    output = [0 for i in range(len(numbers))]
    count = [0 for i in range(256)]
    answer = ["" for _ in numbers]

    for i in numbers:
        count[ord(i)] += 1

    for i in range(256):
        count[i] += count[i - 1]

    for i in range(len(numbers)):
        output[count[ord(numbers[i])] - 1] = numbers[i]
        count[ord(numbers[i])] -= 1

    for i in range(len(numbers)):
        answer[i] = output[i]
    return answer


if __name__ == '__main__':
    print(counting_sort('Hello world'))