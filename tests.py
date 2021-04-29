import unittest
from calculator import *

class CalcTest(unittest.TestCase):
    def test_add(self):
        result = add(5, 8)
        self.assertEqual(result, 13)

    def test_subtract(self):
        result = subtract(5, 8)
        self.assertEqual(result, -3)

    def test_multiply(self):
        result = multiply(5, 8)
        self.assertEqual(result, 40)

    def test_divide(self):
        result = divide(5, 8)
        self.assertEqual(result, 5 / 8)

if __name__ == "__main__":
    unittest.main()