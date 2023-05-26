from classes.guest import *
from classes.room import *
from classes.food import *
from classes.drink import *

class Bar:
    def __init__(self, drinks, foods):
        self.room_take = 0
        self.customer_tab = {}
        self.room_tab = {}
        self.drinks = drinks
        self.foods = foods