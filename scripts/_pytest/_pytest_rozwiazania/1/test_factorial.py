import pytest
from factorial import factorial


def test_factorial_zero():
    """Test that factorial of zero returns one"""
    assert factorial(0) == 1


@pytest.mark.parametrize("n,expected", [
    (1, 1), (2, 2), (3, 6), (4, 24), (5, 120)
])
def test_factorial_small_numbers(n, expected):
    """Test factorials for small numbers: 1! through 5!"""
    assert factorial(n) == expected


def test_factorial_five_specific():
    """Test specifically that factorial of 5 returns 120"""
    assert factorial(5) == 120


def test_negative_number_raises_error():
    """Test that negative number raises ValueError with appropriate message"""
    with pytest.raises(ValueError, match="n must be >= 0"):
        factorial(-1)


def test_non_integer_float_raises_error():
    """Test that non-integer float raises ValueError"""
    with pytest.raises(ValueError, match="n must be exact integer"):
        factorial(30.1)


def test_integer_float_works():
    """Test that integer float works the same as integer"""
    assert factorial(5.0) == 120
    assert factorial(5.0) == factorial(5)


def test_very_large_number_raises_error():
    """Test that very large number raises OverflowError"""
    with pytest.raises(OverflowError, match="n too large"):
        factorial(1e100)