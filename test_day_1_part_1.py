import unittest

def calculate_fuel(i):
    return i // 3 - 2

class Test(unittest.TestCase):
    def test_calculate_fuel(self):
         # Test with a mass of 12.
         self.assertEqual(calculate_fuel(12), 2)
         # Test with a mass of 14.
         self.assertEqual(calculate_fuel(14), 2)
         # Test with a mass of 1969.
         self.assertEqual(calculate_fuel(1969), 654)
         # Test with a mass of 100756.
         self.assertEqual(calculate_fuel(100756), 33583)
