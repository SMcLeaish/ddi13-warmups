import time
from typing import Callable


def second_largest(lst: list[int]) -> int | None:
    try:
        return sorted(set(lst))[-2]
    except (IndexError, TypeError) as e:
        print(f'{e}\nexpected a list of at least two integers')
        return None


def split_search(lst: list[int]) -> int | None:
    mid = len(lst) // 2
    lst1 = lst[mid:]
    lst2 = lst[:mid]
    lst1_max = max(lst1)
    lst2_max = max(lst2)
    return second_largest(lst1 if lst1_max > lst2_max else lst2)


def timer(func: Callable[[list[int]], int | None], lst: list[int]) -> None:
    start_time = time.perf_counter()
    result = func(lst)
    stop_time = time.perf_counter()
    print(f'Result: {result}')
    print(f'Elapsed time: {stop_time - start_time:.6f} seconds')


timer(second_largest, list(range(1, 10000)))
timer(split_search, list(range(1, 10000)))
