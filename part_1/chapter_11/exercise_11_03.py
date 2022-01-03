# Exercise 11-3

import unittest

class Employee:
    """Initialize Employee"""

    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary
    
    def give_raise(self, increase=5000):
        self.salary += increase


class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.my_info = Employee('dimitris', 'ch', 11_000)

    def test_give_default_raise(self):
        self.my_info.give_raise()
        self.assertEqual(self.my_info.salary, 16000)
    
    def test_give_custom_raise(self):
        self.my_info.give_raise(2000)
        self.assertEqual(self.my_info.salary, 13000)

if __name__ == '__main__':
    unittest.main()