"""Поиск всех простых чисел до натурального числа <x>"""


def sieve_of_eratosthenes(x: int) -> list:
    pattern = [1] * (x - 1)
    numbers = list()

    for i in range(2, int(x / 2)):
        t = 2 * i

        while t <= x:
            pattern[t - 2] = 0
            t += i

    for i in range(len(pattern)):
        if pattern[i] != 0:
            numbers.append(i + 2)

    return numbers


def test_sieve_of_eratosthenes():
    test_value = {
        10: [2, 3, 5, 7],
        28: [2, 3, 5, 7, 11, 13, 17, 19, 23],
        47: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    }
    for number in test_value:
        answer = sieve_of_eratosthenes(number)
        assert answer == test_value[number]


if __name__ == '__main__':
    test_sieve_of_eratosthenes()
