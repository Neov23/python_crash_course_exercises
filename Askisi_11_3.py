# Άσκηση 11-3

import unittest
from module__employee import Employee

class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.my_info = Employee('thomas', 'katogios', 11000)

    def test_give_default_raise(self):
        self.my_info.give_raise()
        self.assertEqual(self.my_info.salary, 16000)
    
    def test_give_custom_raise(self):
        self.my_info.give_raise(2000)
        self.assertEqual(self.my_info.salary, 13000)

if __name__ == '__main__':
    unittest.main()