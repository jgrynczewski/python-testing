import unittest
from factorial import factorial


class TestFactorial(unittest.TestCase):
    
    def test_factorial_zero(self):
        """Test that factorial of zero returns one"""
        self.assertEqual(factorial(0), 1)
    
    def test_factorial_small_numbers(self):
        """Test factorials for small numbers: 1! through 5!"""
        params = [(1, 1), (2, 2), (3, 6), (4, 24), (5, 120)]
        for param in params:
            with self.subTest(param=param):
                self.assertEqual(factorial(param[0]), param[1])

    def test_factorial_five_specific(self):
        """Test specifically that factorial of 5 returns 120"""
        self.assertEqual(factorial(5), 120)
    
    def test_negative_number_raises_error(self):
        """Test that negative number raises ValueError with appropriate message"""
        with self.assertRaisesRegex(ValueError, "n must be >= 0"):
            factorial(-1)
    
    def test_non_integer_float_raises_error(self):
        """Test that non-integer float raises ValueError"""
        with self.assertRaisesRegex(ValueError, "n must be exact integer"):
            factorial(30.1)
    
    def test_integer_float_works(self):
        """Test that integer float works the same as integer"""
        self.assertEqual(factorial(5.0), 120)
        self.assertEqual(factorial(5.0), factorial(5))
    
    def test_very_large_number_raises_error(self):
        """Test that very large number raises OverflowError"""
        with self.assertRaisesRegex(OverflowError, "n too large"):
            factorial(1e100)


if __name__ == '__main__':
    unittest.main()
