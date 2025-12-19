import pytest

from car import Car

@pytest.fixture
def car():
    return Car()


def test_speed_at_init(car):
    assert car.speed == 0

def test_set_speed(car):
    car.speed = 10

    assert car.speed == 10

def test_cannot_set_negative_speed(car):
    with pytest.raises(ValueError):
        car.speed = -10
