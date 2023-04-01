import unittest
import numpy as np
from my_module import subtract, multiply, divide, calculate_mean


class TestMyModule(unittest.TestCase):
    def test_subtract(self):
        self.assertEqual(subtract(5, 2), 3)
        self.assertEqual(subtract(0, 0), 0)
        self.assertEqual(subtract(-5, 2), -7)

    def test_multiply(self):
        self.assertEqual(multiply(5, 2), 10)
        self.assertEqual(multiply(0, 0), 0)
        self.assertEqual(multiply(-5, 2), -10)

    def test_divide(self):
        self.assertEqual(divide(5, 2), 2.5)
        self.assertRaises(ValueError, divide, 5, 0)

    def test_calculate_mean(self):
        numbers = [1, 2, 3, 4, 5]
        self.assertEqual(calculate_mean(numbers), np.mean(numbers))


if __name__ == '__main__':
    unittest.main()