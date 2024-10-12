# Import the necessary modules
import unittest
from simple_calculator import SimpleCalculator

# Define a test class that inherits from unittest.TestCase
class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        # Create an instance of the SimpleCalculator class
        self.calculator = SimpleCalculator()

    # Test the add method
    def test_add(self):
        # Test normal operation
        self.assertEqual(self.calculator.add(2, 3), 5)
        # Test edge case: adding zero
        self.assertEqual(self.calculator.add(2, 0), 2)

    # Test the subtract method
    def test_subtract(self):
        # Test normal operation
        self.assertEqual(self.calculator.subtract(5, 3), 2)
        # Test edge case: subtracting zero
        self.assertEqual(self.calculator.subtract(5, 0), 5)

    # Test the multiply method
    def test_multiply(self):
        # Test normal operation
        self.assertEqual(self.calculator.multiply(4, 5), 20)
        # Test edge case: multiplying by zero
        self.assertEqual(self.calculator.multiply(4, 0), 0)

    # Test the divide method
    def test_divide(self):
        # Test normal operation
        self.assertEqual(self.calculator.divide(10, 2), 5)
        # Test edge case: dividing by zero
        with self.assertRaises(ZeroDivisionError):
            self.calculator.divide(10, 0)

if __name__ == '__main__':
    unittest.main()