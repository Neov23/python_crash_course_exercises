# Exercise 11-2

import unittest

from city_functions import city_country

class CityNamesTest(unittest.TestCase):
    """Testing 'city_functions.py' functionality"""
    def test_city_country(self):
        display_city_country = city_country('thessaloniki', 'ellada')
        self.assertEqual(display_city_country, '"Thessaloniki, Ellada"')

    def test_city_country_population(self):
        """Testing 'city_functions.py functionality, population included"""
        display_city_country = city_country('thessaloniki', 'ellada',
        1_000_000)
        self.assertEqual(display_city_country, '"Thessaloniki, Ellada. '
        'Population: 1000000"')

if __name__ == '__main__':
    unittest.main()