from random import randint
import random
from string import ascii_letters, digits
"""Сортировка элементов строки в порядке возрастания с использованием алгоритма сортировки методом подсчета"""


def counting_sort_text(string):
    output = [0 for _ in range(len(string))]
    count = [0 for _ in range(256)]
    answer = ["" for _ in string]

    for i in string:
        count[ord(i)] += 1

    for i in range(256):
        count[i] += count[i - 1]

    for i in range(len(string)):
        output[count[ord(string[i])] - 1] = string[i]
        count[ord(string[i])] -= 1

    for i in range(len(string)):
        answer[i] = output[i]
    return answer


def counting_sort_test():
    n = randint(5, 10)
    text = ''.join(random.choices(ascii_letters + digits, k=n))
    print(f"Original string is:\n{text}")
    print(f"Sorted string is:\n{counting_sort_text(text)}")


if __name__ == '__main__':
    counting_sort_test()
