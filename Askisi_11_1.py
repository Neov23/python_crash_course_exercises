# Άσκηση 11-1

import unittest
from module__city_functions import show_city_country

class CityNamesTest(unittest.TestCase):
    def test_city_country(self):
        city_country = show_city_country('thessaloniki', 'ellada')
        self.assertEqual(city_country, 'Thessaloniki, Ellada')

if __name__ == '__main__':
    unittest.main()