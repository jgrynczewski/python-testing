"""
Stwórz smoka o nazwie "Wawelski"
>>> dragon = Dragon('Wawelski')

Stworzenie smoka bez nazwy podnosi błąd
>>> dragon = Dragon()
Traceback (most recent call last):
    ...
TypeError: Dragon.__init__() missing 1 required positional argument: 'name'

Smok przy tworzeniu ma losowe punkty życia
>>> dragon.health in range(51, 101)
True

Ustaw inicjalną pozycję smoka na x=50, y=100
>>> dragon = Dragon('Wawelski', position_x=50, position_y=100)

Pobierz aktualną pozycję
>>> dragon.get_position()
(50, 100)

Ustaw nową pozycję smoka na x=10, y=20

Przesuń smoka w lewo o 10 i w dół o 20

Przesuń smoka w lewo o 10 i w prawo o 15

Przesuń smoka w prawo o 15 i w górę o 5

Przesuń smoka w dół o 5

Smok zadaje obrażenia (losowo 5-20)

Zadaj 10 obrażeń smokowi

Zadaj 20 obrażeń smokowi

Zadaj 30 obrażeń smokowi

Zadaj 40 obrażeń smokowi

Zadaj 50 obrażeń smokowi

"""

import unittest
from random import randint


class Dragon:
    position_y: int
    position_x: int
    name: str
    health: int

    def __init__(self, name: str, /, *, position_x: int = 0, position_y: int = 0) -> None:
        self.position_x = position_x
        self.position_y = position_y
        self.health = randint(50, 100)
        self.name = name

    def get_position(self) -> tuple[int, int]:
        return self.position_x, self.position_y


class DragonTest(unittest.TestCase):
    def setUp(self):
        self.dragon = Dragon("Wawelski")

    def test_init_name_positional(self):
        self.assertEqual(self.dragon.name, "Wawelski")

    def test_init_name_keyword(self):
        with self.assertRaises(TypeError):
            dragon = Dragon(name="Wawelski")  # noqa

    def test_init_no_name(self):
        with self.assertRaises(TypeError):
            Dragon()  # noqa

    def test_health_init(self):
        self.assertIn(self.dragon.health, range(50, 101))

    def test_init_position_keyword(self):
        dragon = Dragon("Name", position_x=1, position_y=2)
        self.assertEqual(dragon.position_x, 1)
        self.assertEqual(dragon.position_y, 2)

    def test_init_position_positional(self):
        with self.assertRaises(TypeError):
            Dragon('Name', 1, y=2)  # noqa
        with self.assertRaises(TypeError):
            Dragon('Name', 1, 2)  # noqa

    def test_get_position(self):
        self.assertTupleEqual(self.dragon.get_position(), (0, 0))
