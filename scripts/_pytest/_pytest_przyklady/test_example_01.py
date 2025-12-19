# example_01 tests
import pytest

from example_01 import sum_, div


def test_sum_basic():
    assert sum_(1, 2) == 3
    assert sum_(0, 0) == 0
    assert sum_(1.5, 2.8) == 4.3

def test_sum_floating_point():
    assert sum_(0.2, 0.1) == pytest.approx(0.3)


@pytest.mark.parametrize("a,b,expected", [
    (1, 2, 3),
    (3, 4, 7),
    (-4, 4, 0)
])
def test_sum_parametrized_proper(a, b, expected):
    assert sum_(a, b) == expected

def test_div_zero():
    with pytest.raises(ValueError):
        div(4, 0)

    with pytest.raises(ValueError, match="Cannot divide by zero"):
        div(4, 0)
