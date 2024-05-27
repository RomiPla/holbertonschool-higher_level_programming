#!/usr/bin/env python3
import unittest
from task_01_duck_typing import Circle

class TestCircleNegative(unittest.TestCase):
    def test_circle_negative(self):
        with self.assertRaises(ValueError) as context:
            Circle(-5)
        self.assertTrue("Radius cannot be negative" in str(context.exception))

if __name__ == "__main__":
    unittest.main()
