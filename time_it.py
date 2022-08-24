from random import randint
from timeit import repeat
from bubble_sort_alg import bubble_sort
from insertion_sort_alg import insertion_sort


def run_sorting_algorithm(algorithm, numbers):
    setup_code = f"from __main__ import {algorithm}" \
        if algorithm != "sorted" else ""
    stmt = f"{algorithm}({numbers})"
    times = repeat(setup=setup_code, stmt=stmt, repeat=3, number=10)

    print(f"Algorithm: {algorithm}. Minimum execution time: {min(times):.8f}")


ARRAY_LENGTH = 1000


if __name__ == "__main__":
    array = [randint(0, 1000) for i in range(ARRAY_LENGTH)]
    run_sorting_algorithm(algorithm="sorted", numbers=array)
    run_sorting_algorithm(algorithm="bubble_sort", numbers=array)
    run_sorting_algorithm(algorithm="insertion_sort", numbers=array)


