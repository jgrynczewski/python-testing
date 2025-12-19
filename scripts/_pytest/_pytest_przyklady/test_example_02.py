# fikstury, setup_method/teardown_method
from example_02 import BankAccount

import time


class TestBankAccount:
    @classmethod
    def setup_class(cls):
        print("setUpClass")
        cls.test_start_time = time.time()

    @classmethod
    def teardown_class(cls):
        print("tesarDownClass")
        duration = time.time() - cls.test_start_time
        print(f"Testy wykonały się w {duration} czasie")

    def setup_method(self):
        print("setUp")
        self.account = BankAccount(initial_balance=100)


    def teardown_method(self):
        print("tearDown")
        BankAccount.ACCOUNT_COUNTER = 0
        self.account = None  # można, ale nie trzeba

    def test_initial_balance(self):
        assert self.account.balance == 100
        assert  self.account.get_transaction_count() == 0

    def test_deposit_success(self):
        self.account.deposit(100)

        assert  self.account.balance == 200
        assert self.account.get_transaction_count() == 1
        assert "Deposit: +100" in self.account.transaction_history
        assert self.account.ACCOUNT_COUNTER == 1

    def test_withdraw_success(self):
        self.account.withdraw(30)

        assert self.account.balance == 70
        assert self.account.get_transaction_count() == 1
        assert "Withdraw: -30" in self.account.transaction_history
        assert self.account.ACCOUNT_COUNTER == 1
