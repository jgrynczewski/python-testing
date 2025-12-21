# Pytest - Nowoczesny Framework Testowy

## Co to jest pytest?
- **Zewnętrzna biblioteka** - wymaga `pip install pytest`
- **Prostsza składnia** - zwykły `assert`, funkcje zamiast klas
- **Potężne fixtures** - dependency injection zamiast setup/teardown
- **Kompatybilność wsteczna** - uruchamia testy unittest automatycznie

## Podstawy

### Prosty test
```python
def test_add():
    assert sum_(2, 3) == 5

def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)
```

### Uruchamianie
```bash
pytest                           # wszystkie testy
pytest test_module.py            # konkretny plik
pytest -v                       # verbose
pytest -x                       # stop po pierwszym błędzie
pytest -k "test_add"             # tylko testy zawierające "test_add"
```

## Kluczowe asercje

```python
# Podstawowe porównania
assert result == expected
assert result != unexpected
assert result > 10

# Float z tolerancją
assert 0.1 + 0.2 == pytest.approx(0.3)
assert 0.1 + 0.2 == pytest.approx(0.3, abs=1e-5)  # bezwzględna
assert 0.1 + 0.2 == pytest.approx(0.3, rel=1e-5)  # względna

# Wyjątki
with pytest.raises(ValueError):
    function_that_fails()

with pytest.raises(ValueError, match="specific message"):
    function_with_message()
```

## Fixtures - główna zaleta

### Podstawowe fixtures
```python
@pytest.fixture
def bank_account():
    account = BankAccount(100)
    yield account          # jak return + cleanup
    # kod po yield = cleanup
    BankAccount.counter = 0

def test_withdraw(bank_account):
    result = bank_account.withdraw(50)
    assert result == 50
```

### Scope fixtures
```python
@pytest.fixture(scope="function")  # domyślny - nowe dla każdego testu
def fresh_account():
    return BankAccount(100)

@pytest.fixture(scope="class")     # jedno dla całej klasy testowej
def shared_database():
    return Database()

@pytest.fixture(scope="module")    # jedno dla całego pliku
def config():
    return load_config()

@pytest.fixture(scope="session")   # jedno dla całej sesji pytest
def expensive_resource():
    return create_expensive_connection()
```

### Parametryzowane fixtures
```python
@pytest.fixture(params=[100, 200, 500])
def account_with_balance(request):
    return BankAccount(request.param)

# Test uruchomi się 3 razy - dla każdej wartości params
def test_balance(account_with_balance):
    assert account_with_balance.balance > 0
```

## Parametryzacja testów

```python
@pytest.mark.parametrize("a,b,expected", [
    (1, 2, 3),
    (5, 3, 8),
    (-1, 1, 0),
])
def test_sum_parametrized(a, b, expected):
    assert sum_(a, b) == expected

# Każdy przypadek = osobny test w raporcie
# Lepsze niż pętle - widać dokładnie który się niepowodzi
```

## Wbudowane fixtures

### capsys - przechwytywanie output
```python
def test_print_output(capsys):
    print("Hello World")
    captured = capsys.readouterr()
    assert "Hello World" in captured.out
    assert captured.err == ""
```

### tmp_path - tymczasowe pliki
```python
def test_file_operations(tmp_path):
    file_path = tmp_path / "test.txt"
    file_path.write_text("content")
    assert file_path.read_text() == "content"
```

### monkeypatch - proste mockowanie
```python
def test_environment(monkeypatch):
    monkeypatch.setenv("API_KEY", "test_key")
    monkeypatch.setattr("main.requests", mock_requests)
    # test code
```

### caplog - przechwytywanie logów
```python
def test_logging(caplog):
    caplog.set_level(logging.INFO)
    logging.info("Test message")
    assert "Test message" in caplog.messages
```

## Konfiguracja

### conftest.py
```python
# Automatycznie importowane fixtures dla tego folderu i podfolderów
@pytest.fixture
def shared_fixture():
    return "shared data"

# Hooks i konfiguracja
def pytest_configure(config):
    config.addinivalue_line("markers", "slow: marks tests as slow")
```

### pytest.ini
```ini
[pytest]
minversion = 6.0
testpaths = tests src
python_files = test_*.py *_test.py

markers =
    slow: marks tests as slow
    integration: marks tests as integration
    unit: marks tests as unit tests

addopts = 
    -ra
    --strict-markers
    --cov=src
    --cov-report=html
    --cov-fail-under=80

log_cli = true
log_level = INFO
```

## Markery

### Wbudowane
```python
@pytest.mark.skip("Nie gotowe")
def test_future_feature():
    pass

@pytest.mark.skipif(sys.platform == "win32", reason="Unix only")  
def test_unix_feature():
    pass

@pytest.mark.xfail(reason="Znany bug")
def test_known_issue():
    assert buggy_function() == "correct"
```

### Własne markery
```python
@pytest.mark.slow
def test_heavy_computation():
    pass

@pytest.mark.integration  
def test_database_connection():
    pass

# Uruchamianie
pytest -m slow              # tylko slow
pytest -m "not slow"        # bez slow
pytest -m "slow or unit"    # slow LUB unit
```

## Mocking

### unittest.mock (kompatybilny)
```python
from unittest.mock import patch, MagicMock

@patch('main.requests')
def test_api_call(mock_requests):
    mock_requests.get.return_value.status_code = 200
    # test
```

### monkeypatch (wbudowane)
```python
def test_with_monkeypatch(monkeypatch):
    mock_response = MagicMock()
    monkeypatch.setattr("main.requests.get", lambda url: mock_response)
    # test - bez zewnętrznych zależności
```

### pytest-mock (plugin)
```bash
pip install pytest-mock
```
```python
def test_with_mocker(mocker):
    mock_requests = mocker.patch("main.requests")
    mock_requests.get.return_value.status_code = 200
    # test
```

## Coverage

### Instalacja
```bash
pip install pytest-cov
```

### Podstawowe użycie
```bash
pytest --cov=src                    # basic coverage
pytest --cov=src --cov-report=html  # HTML report
pytest --cov=src --cov-branch       # branch coverage  
pytest --cov-fail-under=80          # fail jeśli < 80%
```

### Konfiguracja w pytest.ini
```ini
addopts = 
    --cov=src
    --cov-branch
    --cov-report=term-missing
    --cov-report=html:htmlcov
    --cov-fail-under=80
```

## Struktura projektu
```
_pytest/
├── _pytest_przyklady/           # Przykłady demonstracyjne
│   ├── conftest.py             # Współdzielone fixtures
│   ├── pytest.ini             # Konfiguracja
│   ├── test_*.py               # Testy podstawowe
│   ├── coverage/               # Przykłady coverage
│   ├── hooks/                  # Custom hooks i pluginy
│   └── mocking/                # Przykłady mockowania
├── _pytest_zadania/             # Ćwiczenia do rozwiązania  
├── _pytest_rozwiazania/         # Gotowe rozwiązania
└── README.md
```

## Różnice względem unittest

| Aspect | unittest | pytest |
|--------|----------|--------|
| **Struktura** | Klasy `TestCase` | Funkcje `test_*` |
| **Setup** | `setUp/tearDown` | fixtures z `yield` |
| **Asercje** | `self.assertEqual()` | `assert ==` |
| **Parametryzacja** | `subTest` | `@pytest.mark.parametrize` |
| **Mocking** | `@patch` | `monkeypatch` + kompatybilność |
| **Uruchamianie** | `python -m unittest` | `pytest` |

## Dobre praktyki

### 1. Fixtures zamiast setup/teardown
```python
# LEPSZE - pytest
@pytest.fixture
def prepared_data():
    data = create_test_data()
    yield data
    cleanup_data(data)

# Gorsze - unittest style  
def setUp(self):
    self.data = create_test_data()

def tearDown(self):
    cleanup_data(self.data)
```

### 2. Parametryzacja zamiast pętli
```python
# LEPSZE - każdy przypadek to osobny test
@pytest.mark.parametrize("input,expected", [(1, 2), (3, 6)])
def test_function(input, expected):
    assert function(input) == expected

# Gorsze - jeden test, trudny debugging
def test_function():
    for input, expected in [(1, 2), (3, 6)]:
        assert function(input) == expected
```

### 3. Organizacja fixtures
- **conftest.py** - dla współdzielonych fixtures
- **Odpowiedni scope** - function/class/module/session
- **Cleanup przez yield** - zamiast explicit teardown

### 4. Coverage
- **80% to dobry cel** - nie 100%
- **Branch coverage** lepsze niż line coverage
- **HTML report** najlepszy - pokazuje co nie jest testowane

## Najczęstsze błędy
1. **Zbyt szeroki scope fixtures** - session gdy wystarczy function
2. **Brak cleanup w fixtures** - pamięć o `yield` i sprzątaniu
3. **Nieużywanie parametryzacji** - pętle w testach zamiast `@pytest.mark.parametrize`
4. **Niezarejestrowane markery** - ostrzeżenia, użyj `pytest.ini`
5. **Złe miejsce conftest.py** - fixtures dostępne tylko w tym i podkatalogach

Pytest to nowoczesny, elastyczny framework który znacznie upraszcza pisanie i utrzymywanie testów dzięki fixtures, prostej składni i bogatemu ekosystemowi pluginów.