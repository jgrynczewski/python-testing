# Doctest - Testowanie w Dokumentacji

## Co to jest Doctest?
- **Dokumentacja z testami** - testy wbudowane w docstringi
- **Interaktywna sesja** - format `>>> kod` jak w interpreterze  
- **Narzędzie dokumentacyjne** - przede wszystkim do dokumentacji!

## Główne zalety Doctest
- **Żywa dokumentacja** - uzupełnia dokumentację o interaktywne przypadki użycia
- **Synchronizacja** - pomaga w utrzymaniu aktualnej dokumentacji (zmiana API → błąd doctest → aktualizacja docs)
- **Przykłady użycia** - pokazuje rzeczywiste wywołania funkcji/klas
- **Łatwość pisania** - format copy-paste z interpretera

## ⚠️ Ważne ograniczenia
Doctest **nie zastępuje właściwych testów**:
- **Nie wystarczy** do kompletnego testowania aplikacji
- **Uzupełnia, nie zastępuje** unittest/pytest  
- **Sprawdza się do** prostych przykładów API i edge cases
- **Nie nadaje się do** złożonej logiki biznesowej i integration testów

## Struktura projektu
```
_doctest/
├── _doctest_przyklady/        # Przykłady demonstracyjne
│   ├── example_01.py         # Podstawowe funkcje i składnia
│   ├── example_02.py         # Testowanie klas
│   ├── example_03.py         # Kompletny przykład z modułem
│   ├── example_04.py         # Sposoby uruchamiania
│   ├── example_05.py         # Pułapki i edge cases  
│   ├── example_06.py         # Flagi i dyrektywy
│   ├── example_07.py         # Doctest internals
│   ├── example_08.py         # Testowanie zewnętrznych bibliotek
│   ├── context.py            # Klasy pomocnicze
│   └── tests                 # Zewnętrzny plik z testami
├── _doctest_zadania/          # Ćwiczenia do rozwiązania
│   ├── exercise_01.py        # Funkcja factorial z TODO
│   └── exercise_02.py        # Klasa DataProcessor z TODO
├── _doctest_rozwiazania/      # Gotowe rozwiązania
│   ├── exercise_01.py        # Kompletne testy factorial
│   └── exercise_02.py        # Kompletne testy DataProcessor
└── README.md
```

## Podstawy

### Mechanizm działania
- Doctest wyszukuje w docstringach wzorca linii sesji interpretera (`>>>`)
- Wykonuje znalezione linie i porównuje output z zapisanym wynikiem
- Testy muszą być identyczne znak po znak z outputem interpretera

### Podstawowe uruchamianie
```bash
python3 -m doctest plik.py          # cichy tryb (tylko błędy)
python3 -m doctest plik.py -v       # verbose (wszystkie wyniki)
```

```python
if __name__ == "__main__":
    import doctest
    doctest.testmod()                # uruchomi wszystkie testy w module
    doctest.testmod(verbose=True)    # z pełnym outputem
```

## Pisanie testów

### Podstawowa składnia
```python
def sum_(a, b):
    """
    Dodaje dwie liczby.
    
    >>> sum_(1, 2)
    3
    >>> sum_(-1, 1)  
    0
    """
    return a + b
```

### Testy wielolinijkowe
```python
def process_data():
    """
    >>> a = 1
    >>> b = 2
    >>> sum_(a, b)
    3
    >>> sum_(a, 4)  # stan jest przechowywany między testami
    5
    """
```

### Bloki kodu
```python
def calculate():
    """
    >>> res = 0
    >>> for t in [(1, 2), (3, 4)]:
    ...     res += sum_(t[0], t[1])
    >>> res
    10
    """
```

## Obsługa wyjątków

### Prawidłowy format
```python
def divide(a, b):
    """
    >>> divide(4, 0)
    Traceback (most recent call last):
        ...
    ValueError: Cannot divide by zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b
```

## Testowanie klas

### Kompletny przykład
```python
class Calculator:
    """
    Tworzenie instancji:
    >>> calc = Calculator()
    >>> calc.result
    0
    
    Operacje:
    >>> calc.add(5)
    5
    >>> calc.add(3)
    8
    """
    
    def __init__(self):
        self.result = 0
        
    def add(self, value):
        """
        >>> calc = Calculator()
        >>> calc.add(5)
        5
        """
        self.result += value
        return self.result
```

## Ważne pułapki

### 1. Precyzja floatów
```python
# ZŁE - nieprzewidywalny wynik
>>> 0.1 + 0.2  # doctest: +SKIP
0.3

# DOBRE - zaokrąglanie
>>> round(0.1 + 0.2, 1)
0.3

# DOBRE - porównanie z tolerancją  
>>> abs(0.1 + 0.2 - 0.3) < 0.00001
True
```

### 2. Reprezentacja stringów
```python
# ZŁE - interpreter używa apostrofów
>>> "Hello"  # doctest: +SKIP  
"Hello"

# DOBRE
>>> "Hello"
'Hello'
```

### 3. Losowość
```python
def generate_data():
    """
    >>> import random
    >>> random.seed(42)  # deterministyczne wyniki
    >>> generate_data(3)
    [10, 1, 0]
    """
    return [random.randint(0, 10) for _ in range(3)]
```

### 4. Kolejność w setach
```python
# ZŁE - niezdeterminowana kolejność
>>> {3, 1, 2}  # doctest: +SKIP
{3, 1, 2}

# DOBRE - testowanie zawartości
>>> s = {3, 1, 2}
>>> 1 in s
True
>>> sorted(s)
[1, 2, 3]
```

### 5. Adresy obiektów
```python
# ZŁE - zmienny adres
>>> object()  # doctest: +SKIP
<object object at 0x...>

# DOBRE - typ obiektu
>>> obj = object()
>>> type(obj).__name__
'object'
```

## Flagi i dyrektywy

### Najważniejsze flagi
```python
def example():
    """
    # SKIP - pomija test
    >>> 1/0  # doctest: +SKIP
    0
    
    # ELLIPSIS - zastępuje ... dowolnym tekstem
    >>> object()  # doctest: +ELLIPSIS
    <object object at 0x...>
    
    # NORMALIZE_WHITESPACE - ignoruje dodatkowe spacje
    >>> print("Hello    World")  # doctest: +NORMALIZE_WHITESPACE
    Hello World
    
    # IGNORE_EXCEPTION_DETAIL - ignoruje szczegóły wyjątków
    >>> 1/0  # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
        ...
    ZeroDivisionError: any message
    
    # Kombinowanie flag
    >>> import uuid
    >>> str(uuid.uuid4())  # doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
    '...-...-...-...-...'
    """
```

### Sposoby stosowania flag
```python
# 1. Inline (pojedynczy test)
>>> test()  # doctest: +ELLIPSIS

# 2. Wiersz poleceń (cały plik)
python -m doctest plik.py -o ELLIPSIS -o NORMALIZE_WHITESPACE

# 3. Parametr funkcji (cały moduł)
doctest.testmod(optionflags=doctest.ELLIPSIS | doctest.NORMALIZE_WHITESPACE)
```

## Komentowanie

```python
def example():
    """
    >>> sum_(1, 2)
    3
    
    UWAGA! Brak odstępu przed komentarzem sprawi, że zostanie potraktowany
    jako część outputu poprzedniego testu:
    # >>> sum_(1, 2)  # ZAKOMENTOWANY TEST
    # 0
    
    Można komentować dowolnym znakiem przed >>>:
    a >>> sum(1, 2)  # ZAKOMENTOWANY
    """
```

## Sposoby uruchamiania

### 1. Cały moduł
```python
# Z linii poleceń
python3 -m doctest example.py
python3 -m doctest example.py -v

# W kodzie
if __name__ == "__main__":
    doctest.testmod()
    doctest.testmod(verbose=True)
```

### 2. Wybrane elementy
```python
import doctest

# Tylko testy modułowe (z górnego docstringa)
doctest.run_docstring_examples(module, globs=globals(), verbose=True)

# Pojedyncza funkcja
doctest.run_docstring_examples(funkcja, globals(), verbose=True)

# Pojedyncza klasa (wszystkie metody)
doctest.run_docstring_examples(Klasa, globals(), verbose=True)

# Pojedyncza metoda
doctest.run_docstring_examples(Klasa.metoda, globals(), verbose=True)
```

### 3. Z pliku tekstowego
```python
# Plik "tests" z testami w formacie doctest
with open("tests") as f:
    tests = f.read()

import context  # moduł z potrzebną funkcjonalnością
doctest.run_docstring_examples(tests, vars(context))

# Lub bezpośrednio
doctest.testfile("tests", globs=vars(context))
```

### 4. Z dodatkowym kontekstem
```python
# Dodanie dodatkowych zmiennych/funkcji do testów
doctest.testmod(verbose=True, extraglobs={'helper': lambda x: x**2})
```

## Testowanie z zewnętrznych bibliotek
```python
import fractions
import doctest

# Uruchom testy z biblioteki standardowej
doctest.testmod(fractions, verbose=True)
```

## Dobre praktyki

### 1. Struktura testów
- Umieść testy modułowe w docstringu na górze pliku
- Dodaj testy do każdej funkcji/metody w ich docstringach  
- Testuj typowe przypadki użycia i przypadki brzegowe
- Zawsze testuj obsługę błędów

### 2. Czytelność
- Grupuj powiązane testy
- Używaj opisowych komentarzy
- Przykłady powinny być jednocześnie testami i dokumentacją

### 3. Niezawodność  
- Unikaj testów zależnych od czasu/losowości (lub kontroluj je)
- Używaj flag gdy to konieczne
- Pamiętaj o precyzji floatów
- Stan jest współdzielony między testami w tym samym docstringu

### 4. Obsługa błędów czasów
```python
def test_time():
    """
    # Testuj typ
    >>> isinstance(get_timestamp(), float)
    True
    
    # Testuj że jest "świeży"
    >>> import time
    >>> abs(get_timestamp() - time.time()) < 1.0
    True
    
    # Testuj względem znanej daty
    >>> get_timestamp() > 1600000000  # > 2020
    True
    
    # Unikaj mockowania w doctestach (wpływa na inne testy)
    """
```

## Struktura foldera

- `_doctest_przyklady/` - Przykłady demonstrujące wszystkie aspekty doctest
- `_doctest_zadania/` - Ćwiczenia do samodzielnego rozwiązania  
- `_doctest_rozwiazania/` - Gotowe rozwiązania zadań

Doctest to doskonałe narzędzie do prostych testów i dokumentacji jednocześnie. Sprawdza się szczególnie dobrze do testowania API funkcji i przykładów użycia.