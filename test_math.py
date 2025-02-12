import unittest
import math_lib  # Importing the math module

class TestMathFunctions(unittest.TestCase):
    def test_add(self):
        self.assertEqual(math_lib.add(3, 4), 7)
        self.assertEqual(math_lib.add(-1, 1), 0)
        self.assertEqual(math_lib.add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(math_lib.subtract(10, 4), 6)
        self.assertEqual(math_lib.subtract(0, 5), -5)
        self.assertEqual(math_lib.subtract(3, 3), 0)

if __name__ == "__main__":
    unittest.main()
