from random import randint
from timeit import repeat
import statistics
from multiprocessing.pool import ThreadPool
import time
from bubble_sort_alg import bubble_sort
from insertion_sort_alg import insertion_sort
from merge_sort_alg import merge_sort


ARRAY_LENGTH = 1000

array = [randint(0, 100) for i in range(ARRAY_LENGTH)]


def run_sorting_algorithm(algorithm, numbers=None):
    if numbers is None:
        numbers = array
    setup_code = f"from __main__ import {algorithm}" \
        if algorithm != "sorted" else ""
    stmt = f"{algorithm}({numbers})"
    times = repeat(setup=setup_code, stmt=stmt, repeat=10, number=10)

    print(
        f"Algorithm: {algorithm}."
        f" Min exec time: {min(times):.8f}."
        f" Maximum exec time: {max(times):.8f}."
        f" Avg exec time: {statistics.fmean(times):.8f}")


def single_process_run():
    print("Single process function started!")
    n = time.process_time()
    run_sorting_algorithm(algorithm="sorted")
    run_sorting_algorithm(algorithm="insertion_sort")
    run_sorting_algorithm(algorithm="bubble_sort")
    run_sorting_algorithm(algorithm="merge_sort")
    elapsed_time2 = time.process_time() - n
    print(f"Time from start: {elapsed_time2}")
    return elapsed_time2


def multi_process_run():
    print("Multi process function started!")
    t = time.process_time()
    pool = ThreadPool()
    params = ["sorted", "bubble_sort", "insertion_sort", "merge_sort"]
    pool.map(run_sorting_algorithm, params)
    elapsed_time = time.process_time() - t
    print(f"Time from start: {elapsed_time}")
    return elapsed_time


if __name__ == "__main__":
    elapsed_time_single = single_process_run()
    print("==================================================================")
    elapsed_time_multi = multi_process_run()
    print("--------------------\nRun with multi-process {0} then single-process on: {1}".format(
        "faster" if elapsed_time_single - elapsed_time_multi >= 0 else "slower",
        elapsed_time_single - elapsed_time_multi if elapsed_time_single >= elapsed_time_multi
        else elapsed_time_multi - elapsed_time_single))
