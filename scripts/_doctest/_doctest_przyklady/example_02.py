# Docktesty klas
class Calculator:
    """
    Prosta klasa kalkulatora z doctest.
    """

    def __init__(self):
        self.result = 0

    def add(self, value):
        """Add value to current result.
        
        Args:
            value: Number to add to current result
            
        Returns:
            Updated result after addition
        """
        self.result += value
        return self.result

    def divide(self, value):
        """Divide current result by value.
        
        Args:
            value: Number to divide current result by
            
        Returns:
            Updated result after division
            
        Raises:
            ValueError: If value is zero
        """
        if value == 0:
            raise ValueError("Cannot divide by zero.")
        self.result /= value
        return self.result

    def clear(self):
        """Reset current result to zero.
        
        Returns:
            Result after clearing (always 0)
        """
        self.result = 0
        return self.result
