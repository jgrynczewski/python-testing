"""
Stwórz smoka o nazwie "Wawelski"
>>> dragon = Dragon("Wawelski")

Stworzenie smoka bez nazwy podnosi błąd
>>> dragon=Dragon()
Traceback (most recent call last):
...
TypeError: Dragon.__init__() missing 1 required positional argument: 'name'

Smok przy tworzeniu ma losowe punkty życia
>>> import random
>>> random.seed(22)
>>> dragon=Dragon("")
>>> dragon.health
18


Ustaw inicjalną pozycję smoka na x=50, y=100
>>> dragon=Dragon("A", 50, 100)
>>> dragon.get_position()
(50, 100)

Pobierz aktualną pozycję
>>> dragon=Dragon("A", 1, 2)
>>> dragon.get_position()
(1, 2)

Ustaw nową pozycję smoka na x=10, y=20
>>> dragon=Dragon("A")
>>> dragon.set_position(10, 20)
>>> dragon.get_position()
(10, 20)

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
import random
import unittest
import pytest



class Dragon:
    HEALTH_MAX = 100
    HEALTH_MIN = 1
    INIT_POS_X = 50
    INIT_POS_Y = 100

    def __init__(self, name, position_x = INIT_POS_X, position_y = INIT_POS_Y, /, initiative = 0):
        self.name = name
        self.health = random.randint(self.HEALTH_MIN, self.HEALTH_MAX)
        self._position_x = position_x
        self._position_y = position_y
        self.is_alive = True
        self.initiative = initiative
        self.dropped_gold = 0

    @property
    def position_x(self):
        return self._position_x

    @position_x.setter
    def position_x(self, value):
        self._position_x = value

    @property
    def position_y(self):
        return self._position_y

    @position_y.setter
    def position_y(self, value):
        self._position_y = value

    def get_position(self) -> tuple[int, int]:
        return self.position_x, self.position_y


    def set_position(self, x, y):
        self.position_x = x
        self.position_y = y

    def change_position(self, /, left=0, right=0, down=0,up=0,):
        self.position_x -= left
        self.position_x += right
        self.position_y -= down
        self.position_y += up

    def make_damage(self) -> int:
        damage = random.randint(5, 20)
        print(f"Dragon {self.name} makes {damage} damage!")
        return damage

    def take_damage(self, damage: int) -> None:
        self.health -= damage
        print(f"Dragon {self.name} takes {damage} damage!")
        if self.health <= 0:
            self._dragon_dies()
        else:
            print(f"Dragon {self.name} remains with {self.health} health!")

    def _dragon_dies(self):
        self.health = 0
        self.is_alive = False
        self._drop_gold()
        print(f"Dragon {self.name} is dead")

    def _drop_gold(self):
        gold = random.randint(1, 100)
        print(f"Dragon {self.name } dropped {gold} gold!")
        self.dropped_gold = gold
        return gold


class DragonTest(unittest.TestCase):

    def tearDown(self):
        self.dragon = None

    def test_init_name_positional(self):
        dragon = Dragon("Wawelski")
        self.assertEqual(dragon.name, "Wawelski")

    def test_init_name_keyword(self):
        with self.assertRaises(TypeError):
            Dragon(name="Wawelski")  # noqa

    def test_init_no_name(self):
        with self.assertRaises(TypeError):
            Dragon()  # noqa

    def test_dragon_random_health(self):
        random.seed = 123
        dragon = Dragon("Wawelski")
        assert 100 > dragon.health > 0

    def test_initial_position(self):
        dragon = Dragon("Wawelski")
        assert dragon.position_x == 50
        assert dragon.position_y == 100

    def test_get_position(self):
        dragon = Dragon("Wawelski", 1, 2)
        assert dragon.get_position() == (1, 2)

    def test_set_position(self):
        dragon = Dragon("Wawelski")
        dragon.set_position(10, 20)
        assert dragon.get_position() == (10, 20)



    def test_change_position(self):
        dragon = Dragon("Wawelski", 0, 0)
        for param in [(10, 0, 20, 0), (10, 15, 0, 0), (0, 0, 5, 0)]:
            with self.subTest(params=param):
                dragon.set_position(0, 0)
                dragon.change_position(left=param[0], right=param[1], down=param[2], up=param[3])
                assert dragon.position_x == 0 - param[0] + param[1]
                assert dragon.position_y == 0 - param[2] + param[3]

    def test_make_damage(self):
        dragon = Dragon("Wawelski", 0, 0)
        assert 20 >= dragon.make_damage() >= 5

    def test_take_damage(self):
        dragon = Dragon("Wawelski", 0, 0)
        dragon.health = 30
        damage = 10
        dragon.take_damage(damage)
        assert dragon.health == 20

    def test_dragon_can_die(self):
        dragon = Dragon("Wawelski")
        for param in [(50), (51) ]:
            with self.subTest(params=param):
                dragon.health = 50
                dragon.take_damage(param)
                assert dragon.health == 0
                assert not dragon.is_alive

def test_dragon_is_dead_msg(capsys):
    dragon = Dragon("Wawelski")
    dragon._dragon_dies()
    captured = capsys.readouterr()
    assert f"Dragon {dragon.name} is dead" in captured.out

def test_dead_dragon_drop_gold( capsys):
    dragon = Dragon("Wawelski")
    dragon._dragon_dies()
    dropped_gold = dragon.dropped_gold
    assert 100 >= dropped_gold >= 1
    captured = capsys.readouterr()
    assert f"dropped {dropped_gold} gold!" in captured.out
