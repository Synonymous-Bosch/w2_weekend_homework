import unittest
from classes.drink import *

class TestDrink(unittest.TestCase):
    def setUp(self):
        self.drink = Drink("Wang wang", 5.50)

    def test_drink_has_name(self):
        self.assertEqual("Wang wang", self.drink.name)

    def test_drink_has_price(self):
        self.assertEqual(5.50, self.drink.price)