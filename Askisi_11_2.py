# Άσκηση 11-2

import unittest
from module__city_functions import show_city_country

class CityNamesTest(unittest.TestCase):
    def test_city_country(self):
        city_country = show_city_country('thessaloniki', 'ellada')
        self.assertEqual(city_country, 'Thessaloniki, Ellada')

    def test_city_country_population(self):
        city_country = show_city_country('thessaloniki', 'ellada',
        1000000)
        self.assertEqual(city_country, 'Thessaloniki, Ellada '
        '- population 1000000')

if __name__ == '__main__':
    unittest.main()