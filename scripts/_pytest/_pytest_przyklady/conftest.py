from example_02 import BankAccount

import time
import pytest


@pytest.fixture(scope="class")
def session_info():
    print("setUpClass")
    test_start_time = time.time()

    yield

    print("tesarDownClass")
    duration = time.time() - test_start_time
    print(f"Testy wykonały się w {duration} czasie")


@pytest.fixture()
def bank_account():
    # przed testem
    print("setUp")
    account = BankAccount(initial_balance=100)

    yield account

    # po teście
    print("tearDown")
    BankAccount.ACCOUNT_COUNTER = 0
    account = None  # można, ale nie trzeba
