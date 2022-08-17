"""Нахождение НОД (наибольший общий делитель) натуральных числе <x> и <y>."""


def euclidean_alg(x: int, y: int) -> int:
    while (x != 0) & (y != 0):
        if x < y:
            y %= x
        else:
            x %= y

    return x + y


def test_euclidean_alg():
    test_values = {
        (10, 6): 2,
        (24, 5): 1,
        (27, 9): 9,
        (105, 30): 15,
        (240, 44): 4
    }
    for pair in test_values:
        x, y = pair
        answer = euclidean_alg(x, y)
        assert answer == test_values[pair]


if __name__ == '__main__':
    test_euclidean_alg()
