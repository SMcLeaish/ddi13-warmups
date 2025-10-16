"""Runs classic code challenge fizzbuzz with command line args."""

import sys

start = int(sys.argv[1])
stop = int(sys.argv[2])


def fizzbuzz(num: int) -> int | str:
    """Returns 'fizzbuzz' 'fizz' 'buzz' or the num.

    Args:
        num: int

    Returns:
        'str': str
        'num': num
    """
    f = num % 3 == 0
    b = num % 5 == 0
    fb = "FizzBuzz"
    return f and b and fb[:] or f and fb[:4] or b and fb[4:] or num


def fizzbuzzer(num: int) -> int | str:
    f = num % 3 == 0
    b = num % 5 == 0
    fizz = f and "Fizz"
    buzz = b and "Buzz"
    fizzbuzz = f and b and "FizzBuzz"
    return fizzbuzz or fizz or buzz or num


if __name__ == "__main__":
    # print('\n'.join(str(x) for x in map(fizzbuzz, range(start, stop))))
    print(*map(fizzbuzz, range(start, stop)), sep="\n")
