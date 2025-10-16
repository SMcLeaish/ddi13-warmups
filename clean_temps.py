import secrets
import sys

import numpy as np
from numpy.random import default_rng


def _clean_temps(data: np.ndarray, high: int, low: int) -> np.ndarray:
    return data[(data >= low) & (data <= high)]


def _average_temp(data: np.ndarray) -> np.floating:
    return np.round(np.mean(data), 2)


def _generate_arr(start: int, stop: int, size: int) -> np.ndarray:
    rng = default_rng(secrets.randbits(128))
    return rng.uniform(low=start, high=stop, size=size)


if __name__ == '__main__':
    try:
        start, stop, size, low, high = [int(x) for x in sys.argv[1:]]
        arr = _generate_arr(start, stop, size)
        clean = _clean_temps(arr, high, low)
        print(_average_temp(clean))
    except ValueError as e:
        print(f'{e} \nExpected arguments: start, stop, size, low, high')
