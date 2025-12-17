import math


def factorial(n):
    """Return the factorial of n, where n is an exact integer >= 0.

    Test first 6 factorials (0! through 5!):
    >>> ... # Add test for 1,2,3,4,5
    ...

    Test specific value - calculate factorial of 5:
    >>> ... # Add test for 5
    ...

    Test negative number - should raise ValueError with message "n must be >= 0":
    >>> ... # Add test for -1
    ...

    Test non-integer float - should raise ValueError with message "n must be exact integer":
    >>> ... # Add test for 30.1
    ...

    Test integer float - should work the same as integer:
    >>> ... # Add test for factorial(30.0)
    ...

    Test very large number - should raise OverflowError with message "n too large":
    >>> ... # Add test for factorial(1e100) or similar large number
    ...
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
