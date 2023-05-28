import unittest
from classes.bar import *
from classes.drink import *
from classes.food import *

class TestBar(unittest.TestCase):
    def setUp(self):
        self.guest1 = Guest("Mario Mario", 45.20, "That's Amore")
        self.guest2 = Guest("Luigi Mario", 20.00, "Shaddap Your Face")
        self.drink = Drink("Wang wang", 5.50)
        self.food = Food("Bbq wings", 2.00)
        guests = [self.guest1]
        songs = []
        self.room1 = Room(1, 6, guests, songs)
        self.drinks = [self.drink]
        self.foods = [self.food]
        self.bar = Bar(self.drinks, self.food)
        self.bar.room_take[self.room1] = 20.00
        

    def test_add_guest_to_tab(self):
        self.bar.add_guest_to_tab(self.guest1) 
        self.assertEqual(1, len(self.bar.tab))

    def test_add_money_to_tab(self):
        self.bar.add_money_to_tab(self.guest1, 5.00)
        self.assertEqual(5.00, self.bar.tab[self.guest1])

    def test_check_guest_has_tab(self):
        self.bar.add_guest_to_tab(self.guest1)
        result = self.bar.check_guest_has_tab(self.guest1)
        self.assertEqual(True, result)

    def test_order_drink_on_tab(self):
        self.bar.order_drink_on_tab(self.guest1, self.drink)
        self.assertEqual(5.50, self.bar.tab[self.guest1])

    def test_order_food_on_tab(self):
        self.bar.order_food_on_tab(self.guest1, self.food)
        self.assertEqual(2.00, self.bar.tab[self.guest1])

    def test_pay_tab(self):
        self.bar.order_drink_on_tab(self.guest1, self.drink)
        self.bar.pay_tab(self.guest1, self.room1)
        self.assertEqual(0, self.bar.tab[self.guest1])
        self.assertEqual(39.70, self.guest1.money)

    def test_check_room_take_exists(self):
        self.bar.room_take[self.room1] = 20
        self.bar.check_room_take_exists(self.room1)
        self.assertEqual(20, self.bar.room_take[self.room1])

    def test_check_room_tab(self):
        self.room1.check_in(self.guest2)
        self.bar.add_money_to_tab(self.guest1, 30)
        self.bar.add_money_to_tab(self.guest2, 20)
        self.assertEqual(50, self.bar.check_room_tab(self.room1))

    def test_pay_entry_fee(self):
        self.bar.pay_entry_fee(self.guest2, self.room1)
        self.assertEqual(15.00, self.guest2.money)
        self.assertEqual(25.00, self.bar.room_take[self.room1])

    def test_pay_tab_increase_room_take_value(self):
        self.bar.order_drink_on_tab(self.guest1, self.drink)
        self.bar.pay_tab(self.guest1, self.room1)
        self.assertEqual(0, self.bar.tab[self.guest1])
        self.assertEqual(39.70, self.guest1.money)
        self.assertEqual(25.50, self.bar.room_take[self.room1])