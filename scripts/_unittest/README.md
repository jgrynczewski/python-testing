# Unittest - Framework do Testów Jednostkowych

## Co to jest unittest?
- **Wbudowany framework** - część standardowej biblioteki Pythona
- **Inspirowany JUnit** - klasy testowe dziedziczące z TestCase
- **Zero dependencies** - nie wymaga `pip install`, zawsze dostępny
- **Standard w stdlib** - używany do testowania samej biblioteki standardowej Pythona

## Podstawy

### Struktura testów
```python
import unittest

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()
    
    def test_add_positive_numbers(self):
        result = self.calc.add(2, 3)
        self.assertEqual(result, 5)
    
    def test_divide_by_zero_raises_error(self):
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)

if __name__ == '__main__':
    unittest.main()
```

### Uruchamianie testów
```bash
python -m unittest                    # wszystkie testy  
python -m unittest test_module        # konkretny moduł
python -m unittest -v                 # verbose mode
python test_file.py                   # bezpośrednio
```

## Kluczowe asercje

```python
# Równość i porównania
self.assertEqual(actual, expected)
self.assertNotEqual(actual, unexpected)
self.assertAlmostEqual(0.1+0.2, 0.3)    # dla floatów

# Truth values
self.assertTrue(condition)
self.assertFalse(condition)
self.assertIsNone(value)
self.assertIsNotNone(value)

# Tożsamość obiektów  
self.assertIs(a, b)                      # ta sama referencja
self.assertIsNot(a, b)                   # różne referencje

# Członkostwo
self.assertIn(item, container)
self.assertNotIn(item, container)

# Wyjątki
with self.assertRaises(ValueError):
    function_that_should_fail()

with self.assertRaisesRegex(ValueError, "must be positive"):
    function_with_specific_message()
```

## Setup i teardown

### Cykl życia testów
```python
class TestExample(unittest.TestCase):
    @classmethod
    def setUpClass(cls):              # Raz przed wszystkimi testami
        cls.expensive_resource = connect_to_database()
    
    @classmethod
    def tearDownClass(cls):           # Raz po wszystkich testach  
        cls.expensive_resource.close()
    
    def setUp(self):                  # Przed każdym testem
        self.account = BankAccount(100)
    
    def tearDown(self):               # Po każdym teście
        cleanup_global_state()
```

**Zastosowania:**
- `setUp/tearDown` - świeże obiekty, cleanup stanu
- `setUpClass/tearDownClass` - drogie operacje (DB, pliki)

## Mocking - izolacja zależności

### Podstawowe typy
```python
from unittest.mock import Mock, MagicMock, patch

# Podstawowy mock
mock = Mock()
mock.return_value = "test result"
mock.side_effect = ["first", "second", Exception("error")]

# MagicMock - automatyczne magic methods
magic = MagicMock()
len(magic)  # działa automatycznie!

# Spy - śledzenie prawdziwego obiektu
spy = Mock(wraps=real_object)
```

### Asercje mocków
```python
# Sprawdzanie wywołań
mock.assert_called()
mock.assert_called_once()
mock.assert_called_with("arg1", "arg2")
mock.assert_called_once_with("arg")

# Historia wywołań
from unittest.mock import call
mock.assert_has_calls([call("hello"), call("world")])
```

## Patching - zastępowanie w runtime

### Podstawowe użycie
```python
# Jako decorator
@patch('main.external_api_call')
def test_function(self, mock_api):
    mock_api.return_value = "test data"
    result = my_function()
    self.assertEqual(result, "expected")

# Jako context manager
def test_with_context(self):
    with patch('main.requests') as mock_requests:
        mock_requests.get.return_value.status_code = 200
        # test code
```

### Kluczowe zasady patchingu
- **Patch miejsce użycia**: `@patch('main.get_data')` nie `@patch('api.get_data')`
- **Kolejność parametrów**: patch najwyżej = parametr najdalej z prawej
- **autospec=True**: walidacja interfejsu

## SubTests - parametryzowane testy

```python
def test_factorial_multiple_values(self):
    test_cases = [(0, 1), (1, 1), (5, 120), (3, 6)]
    
    for input_val, expected in test_cases:
        with self.subTest(input=input_val):
            result = factorial(input_val)
            self.assertEqual(result, expected)
```

## Kontrola wykonywania testów

```python
@unittest.skip("Jeszcze nie zaimplementowane")
def test_future_feature(self):
    pass

@unittest.skipIf(sys.platform == "win32", "Nie działa na Windows")
def test_unix_specific(self):
    pass

@unittest.skipUnless(os.path.exists("/usr/bin/git"), "Wymaga git")
def test_git_integration(self):
    pass

@unittest.expectedFailure
def test_known_bug(self):
    self.assertEqual(buggy_function(), "correct_result")
```

## Test Suites - grupowanie testów

```python
def suite():
    suite = unittest.TestSuite()
    
    # Ładowanie konkretnych testów
    suite.addTest(TestCalculator('test_add'))
    
    # Ładowanie całych klas
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestCalculator))
    
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())
```

## Struktura projektu
```
_unittest/
├── _unittest_przyklady/           # Przykłady demonstracyjne
│   ├── assert_intro.py           # Wprowadzenie do asercji
│   ├── example_01.py             # Podstawy unittest
│   ├── test_example_*.py         # Testy do przykładów
│   ├── mocking/                  # Przykłady mockowania
│   └── patching/                 # Przykłady patchingu
├── _unittest_zadania/             # Ćwiczenia do rozwiązania
├── _unittest_rozwiazania/         # Gotowe rozwiązania
└── README.md
```

## Dobre praktyki

### 1. Organizacja testów
- Jedna klasa testowa na klasę/moduł
- Opisowe nazwy: `test_withdraw_insufficient_funds_raises_error`
- Używaj `subTest` dla podobnych przypadków

### 2. Izolacja testów
- Każdy test niezależny - można uruchomić w dowolnej kolejności
- `setUp/tearDown` dla świeżego stanu
- Mocking zewnętrznych zależności

### 3. Mocking vs Dependency Injection
```python
# LEPSZE - Dependency Injection
def process_data(data_source=None):
    if data_source is None:
        data_source = external_api
    return data_source.get_data()

# Test łatwiejszy - bez patchingu
def test_process_data(self):
    mock_source = Mock(return_value="test_data")
    result = process_data(mock_source)
```

### 4. Custom assertions
```python
def assertIsAdult(self, person):
    if not person.is_adult():
        self.fail(f"{person.name} is not adult (age: {person.age})")
```

## Najczęstsze błędy
1. **Testowanie implementacji** zamiast zachowania
2. **Dependency na kolejność testów** - testy nie są izolowane  
3. **Zbyt szeroki patch** - mockowanie całych modułów niepotrzebnie
4. **Brak cleanup** w tearDown - stan wpływa na inne testy
5. **Patch nie w miejscu użycia** - patch import zamiast usage

Unittest to potężne narzędzie do budowania niezawodnych testów - od prostych unit testów po złożone testy integracyjne z mockowaniem zewnętrznych zależności.