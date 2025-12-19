# fikstury conftest
# fikstury


class TestBankAccount:
    def test_initial_balance(self, bank_account, session_info):
        assert bank_account.balance == 100
        assert  bank_account.get_transaction_count() == 0

    def test_deposit_success(self, bank_account):
        bank_account.deposit(100)

        assert  bank_account.balance == 200
        assert bank_account.get_transaction_count() == 1
        assert "Deposit: +100" in bank_account.transaction_history
        assert bank_account.ACCOUNT_COUNTER == 1

    def test_withdraw_success(self, bank_account):
        bank_account.withdraw(30)

        assert bank_account.balance == 70
        assert bank_account.get_transaction_count() == 1
        assert "Withdraw: -30" in bank_account.transaction_history
        assert bank_account.ACCOUNT_COUNTER == 1
