from dragon_max.src.test_game import Dragon

if __name__ == "__main__":


    dragon_1 = Dragon("Wawelski", initiative=1)
    print(f"Dragon Wawelski starts with {dragon_1.health} HP")
    dragon_2 = Dragon("Czarny", initiative=2)
    print(f"Dragon Czarny starts with {dragon_2.health} HP")


    while True:
        dmg = dragon_1.make_damage()
        dragon_2.take_damage(dmg)
        if not dragon_2.is_alive:
            break
        dmg2 = dragon_2.make_damage()
        dragon_1.take_damage(dmg2)
        if not dragon_1.is_alive:
            break