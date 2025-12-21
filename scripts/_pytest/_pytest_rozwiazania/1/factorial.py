import math


def factorial(n):
    """Return the factorial of n, where n is an exact integer >= 0."""
    if not n >= 0:
        raise ValueError("n must be >= 0")
    if math.floor(n) != n:
        raise ValueError("n must be exact integer")
    if n > 2 ** 63 - 1:  # 64-bit signed int (LONG_LONG_MAX)
        raise OverflowError("n too large")

    result = 1
    for i in range(1, int(n) + 1):
        result *= i

    return result