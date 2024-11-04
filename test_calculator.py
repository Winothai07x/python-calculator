import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    # Add the following test methods to the TestCalculator class:

    def test_add_negative(self):
        self.assertEqual(self.calc.add(-1, -2), -3)

    def test_add_zero(self):
        self.assertEqual(self.calc.add(1, 0), 1)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(3, 2), 1)

    def test_subtract_zero(self):
        self.assertEqual(self.calc.subtract(-5, 0), -5)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 3), 6)

    def test_multiply_Negative(self):
        self.assertEqual(self.calc.multiply(-5, 3), -15)

    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 2), 5)

    def test_divide_Negative(self):
        self.assertEqual(self.calc.divide(-10, 5), -2)

    def test_modulo(self):
        self.assertEqual(self.calc.modulo(9, 4), 1)

    def test_modulo_Negative(self):
        self.assertEqual(self.calc.modulo(-20, 7), 1)

if __name__ == '__main__':
    unittest.main()
