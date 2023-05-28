import unittest
from classes.food import *

class TestFood(unittest.TestCase):
    def setUp(self):
        self.food = Food("Bbq wings", 2.00)
    
    def test_food_has_name(self):
        self.assertEqual("Bbq wings", self.food.name)

    def test_food_has_price(self):
        self.assertEqual(2.00, self.food.price)