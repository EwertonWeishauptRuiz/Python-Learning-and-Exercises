import unittest
from circles import circle_area
from math import pi

class TestCircleArea(unittest.TestCase):
    def test_area(self):
        #Test areas when radius is >= 0
        #Assert almost equal will compare the 2 values and if they are equal in 
        #seven decimal places, it will assume they are equal
        self.assertAlmostEqual(circle_area(1), pi)
        self.assertAlmostEqual(circle_area(0), 0)
        self.assertAlmostEqual(circle_area(2.1), pi * 2.1**2)

    def test_values(self):
        # Make sure value errors are raised when necessary 
        # Assert Raises checks for Error raise, argument #1 is the exception class that
        # should be raised, #2 is the function, remaining arguments are inputs to the
        #function
        self.assertRaises(ValueError, circle_area, -2)

    def test_types(self):
        # Make sure errors are raised when the input is not a real number
        # 
        self.assertRaises(ValueError, circle_area, 3+5j)
        self.assertRaises(ValueError, circle_area, True)
        self.assertRaises(ValueError, circle_area, "radius")
