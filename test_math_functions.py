import unittest
from math_functions import add

class TestMathFunctions(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add(1, 2), 3)
        
    def test_add_negative_numbers(self):
        self.assertEqual(add(-1, -1), -2)
        
    def test_add_mixed_numbers(self):
        self.assertEqual(add(-1, 1), 0)
        
    def test_add_zero(self):
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(5, 0), 5)
        self.assertEqual(add(0, 5), 5)

if __name__ == '__main__':
    unittest.main()
