# Pułapki
"""
>>> None  # doctest: +SKIP
None
>>> None
"""

def greet(name):
    """
    znaki identyczne jak w interpreterze
    """
    return f"Witaj {name}!"


def long_text():
    """
    Długie linijki można łamać za pomocą znaku "\"
    """
    return "Very long text " + 52 * "a" + 52 * "b"



# Pułapki doctests
def mistakes():
    """
    Uwaga na precyzję float:

    # Trailing white spaces są czyszczone przez doctest podczas uruchamiania
    """

# Losowość:
# Kontrola nad losowością - wybieramy ziarno (seed) i wtedy zawsze mamy ten sam  "losowy" przebieg

import random


def generate_sample_data(size=5):
    """
    Generuje przykładowe dane do testowania algorytmów

    """
    return [random.randint(0, 10) for _ in range(size)]


def set_order_problem():
    """
    Problem z kolejnością w setach (w dictach od python 3.7 tego problemu już nie ma):

    Lepsze podejście:
    """
    return {3, 1, 2}


def object_id_problem():
    """
    Problem z object id i memory addresses:
    """
    return object()
