# Demonstrating doctest best practices + sposoby uruchamiania
"""
Demonstration module with BankAccount class and helper functions.

Module-level usage examples:

>>> account = BankAccount("TEST001", 100)
>>> account.deposit(50)
150.0
>>> validate_email("test@example.com")
True

Verify class works correctly:
>>> acc = BankAccount("123")
>>> acc.deposit(25)
25.0
>>> acc.withdraw(10)
15.0
"""
import doctest


class BankAccount:
    """
    Represents a bank account.

    Examples:
        Creating account:
        >>> account = BankAccount("12345", 100.0)
        >>> account.account_number
        '12345'
        >>> account.balance
        100.0

        Account operations:
        >>> account.deposit(50)
        150.0
        >>> account.withdraw(30)
        120.0

        Checking balance:
        >>> account.get_balance()
        120.0

        Insufficient funds:
        >>> account.withdraw(200)
        Traceback (most recent call last):
            ...
        ValueError: Insufficient funds
    """

    def __init__(self, account_number, initial_balance=0.0):
        """Initialize new bank account.
        
        Args:
            account_number: Unique identifier for the account
            initial_balance: Starting balance (default 0.0)

        >>> account = BankAccount("54321")
        >>> account.balance
        0.0
        """
        self.account_number = account_number
        self.balance = float(initial_balance)

    def deposit(self, amount):
        """Deposit money to account.
        
        Args:
            amount: Amount to deposit (must be positive)
            
        Returns:
            Updated balance after deposit
            
        Raises:
            ValueError: If amount is not positive

        >>> account = BankAccount("123", 100)
        >>> account.deposit(25)
        125.0

        Invalid amount:
        >>> account.deposit(-10)
        Traceback (most recent call last):
            ...
        ValueError: Amount must be positive
        """
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        """Withdraw money from account.
        
        Args:
            amount: Amount to withdraw (must be positive)
            
        Returns:
            Updated balance after withdrawal
            
        Raises:
            ValueError: If amount is not positive or exceeds balance

        >>> account = BankAccount("123", 100)
        >>> account.withdraw(25)
        75.0
        """
        if amount <= 0:
            raise ValueError("Amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        return self.balance

    def get_balance(self):
        """Return current balance.
        
        Returns:
            Current account balance

        >>> account = BankAccount("123", 42.50)
        >>> account.get_balance()
        42.5
        """
        return self.balance


def validate_email(email):
    """
    Validate email address (simplified version).

    Args:
        email (str): Email address to validate

    Returns:
        bool: True if email is valid

    Examples:
        Valid emails:
        >>> validate_email("user@example.com")
        True
        >>> validate_email("test.user+tag@domain.co.uk")
        True

        Invalid emails:
        >>> validate_email("invalid")
        False
        >>> validate_email("@example.com")
        False
        >>> validate_email("user@")
        False
        >>> validate_email("")
        False

        Edge cases:
        >>> validate_email("a@b.co")
        True
        >>> validate_email("very.long.email.address@very.long.domain.name.com")
        True
    """
    import re
    if not email or not isinstance(email, str):
        return False

    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))
