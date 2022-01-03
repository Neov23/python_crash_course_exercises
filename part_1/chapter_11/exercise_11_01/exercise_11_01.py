# Exercise 11-1

import unittest

from city_functions import city_country

class CityNamesTest(unittest.TestCase):
    """Testing 'city_functions.py' functionality"""
    def test_city_country(self):
        display_city_country = city_country('thessaloniki', 'ellada')
        self.assertEqual(display_city_country, '"Thessaloniki, Ellada"')

if __name__ == '__main__':
    unittest.main()