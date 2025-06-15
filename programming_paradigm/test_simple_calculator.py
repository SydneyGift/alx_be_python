#Script to run unit tests for simple_calculator.py
import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(5, -1), 4)
        self.assertEqual(self.calc.add(-1, -1), -2)
        # Add more assertions to thoroughly test the add method.

    def test_subtraction(self):
        """Test the subtraction method."""
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(-5, 1), -8)
        self.assertEqual(self.calc.subtract(5, -1), 6)
        self.assertEqual(self.calc.subtract(-3, -1), -2)

    def test_multiplication(self):
        """Test the multiplication method."""
        self.assertEqual(self.calc.multiply(5, 3), 15)
        self.assertEqual(self.calc.multiply(-5, 1), -5)
        self.assertEqual(self.calc.multiply(5, -1), -5)
        self.assertEqual(self.calc.multiply(-3, -1), 3)

    def test_division(self):
        """Test the division method."""
        self.assertEqual(self.calc.divide(15, 3), 5)
        self.assertEqual(self.calc.divide(-15, 3), -5)
        self.assertEqual(self.calc.divide(15, -3), -5)
        self.assertEqual(self.calc.divide(-3, -1), 3)
        self.assertEqual(self.calc.divide(3, 0), None)