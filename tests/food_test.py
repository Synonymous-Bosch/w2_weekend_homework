import unittest

class TestFood(unittest.TestCase):
    
    def test_food_has_name(self):
        self.assertEqual("Bbq wings", self.name)

    def test_food_has_price(self):
        self.assertEqual(2.00, self.price)