from random import randint
from timeit import repeat
import statistics
from multiprocessing.pool import ThreadPool
import time

ALGORITHMS = [
        "sorted", "bubble_sort", "insertion_sort", "merge_sort",
        "quick_sort", "shell_sort", "heap_sort", "radix_sort", "counting_sort"]

ARRAY_LENGTH = 2000

array = [randint(0, 1000) for i in range(ARRAY_LENGTH)]


def run_sorting_algorithm(algorithm, numbers=None):
    if numbers is None:
        numbers = array
    setup_code = f"from __main__ import {algorithm}" \
        if algorithm != "sorted" else ""
    stmt = f"{algorithm}({numbers})"
    times = repeat(setup=setup_code, stmt=stmt, repeat=1, number=10)

    print(
        f"Algorithm: {algorithm}."
        f" Min exec time: {min(times):.8f}."
        f" Maximum exec time: {max(times):.8f}."
        f" Avg exec time: {statistics.fmean(times):.8f}")


def single_process_run():
    print("Single process function started!")
    n = time.process_time()
    for func in ALGORITHMS:
        run_sorting_algorithm(algorithm=func)

    elapsed_time2 = time.process_time() - n

    if (elapsed_time2 % 60) >= 1:
        minutes = elapsed_time2 // 60
        seconds = elapsed_time2 - (minutes * 60)
        print(f"Time from start: {elapsed_time2}, minutes = {minutes}, seconds = {seconds}")
    else:
        print(f"Time from start: {elapsed_time2}")

    return elapsed_time2


def multi_process_run():
    print("Multi process function started!")
    t = time.process_time()
    pool = ThreadPool()
    pool.map(run_sorting_algorithm, ALGORITHMS)

    elapsed_time = time.process_time() - t

    if (elapsed_time % 60) >= 1:
        minutes = elapsed_time // 60
        seconds = elapsed_time - (minutes * 60)
        print(f"Time from start: {elapsed_time}, minutes = {minutes}, seconds = {seconds}")
    else:
        print(f"Time from start: {elapsed_time}")
    return elapsed_time


if __name__ == "__main__":
    elapsed_time_single = single_process_run()
    print("=" * 100)
    elapsed_time_multi = multi_process_run()
    print("--------------------\nRun with multi-process {0} then single-process on: {1}".format(
        "faster" if elapsed_time_single - elapsed_time_multi >= 0 else "slower",
        elapsed_time_single - elapsed_time_multi if elapsed_time_single >= elapsed_time_multi
        else elapsed_time_multi - elapsed_time_single))
