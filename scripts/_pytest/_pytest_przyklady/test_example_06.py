# Zastosowanie fikstury request - parametryzowalne fikstury
import pytest


@pytest.fixture(params=[1, 2, 3, 5, 8, 13])
def fib_numbers(request):
    return request.param


def test_fib_is_positive(fib_numbers):
    assert fib_numbers > 0
