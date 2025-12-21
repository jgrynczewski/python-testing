# Doctesty modułów
"""
This is the factorial module.

>>> factorial(4)
24
"""
import math


def factorial(n):
    """Return the factorial of n, where n is an exact integer >= 0.

    Test first 6 factorials (0! through 5!):
    >>> [factorial(n) for n in range(6)] # Add test for 1,2,3,4,5
    [1, 1, 2, 6, 24, 120]

    Test specific value - calculate factorial of 5:
    >>> factorial(30) # Add test for 5
    265252859812191058636308480000000

    Test negative number - should raise ValueError with message "n must be >= 0":
    >>> factorial(-1) # Add test for -1
    Traceback (most recent call last):
    ...
    ValueError: n must be >= 0

    Test non-integer float - should raise ValueError with message "n must be exact integer":
    >>> factorial(30.1) # Add test for 30.1
    Traceback (most recent call last):
    ...
    ValueError: n must be exact integer


    Test integer float - should work the same as integer:
    >>> factorial(30.0) # Add test for factorial(30.0)
    265252859812191058636308480000000

    Test very large number - should raise OverflowError with message "n too large":
    >>> factorial(1e100) # Add test for factorial(1e100) or similar large number
    Traceback (most recent call last):
        ...
    OverflowError: n too large
    """

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
