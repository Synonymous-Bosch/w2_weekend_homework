from classes.guest import *
from classes.room import *
from classes.food import *
from classes.drink import *

class Bar:
    def __init__(self, drinks, foods):
        self.room_take = 0
        self.tab = {}
        self.room_take = {}
        self.drinks = drinks
        self.foods = foods
        self.entry_fee = 5.00

    def check_guest_has_tab(self, guest):
        for key in self.tab:
            if key == guest:
                return True

    def add_guest_to_tab(self, guest):
        self.tab[guest] = 0

    def add_money_to_tab(self, guest, amount):
        if self.check_guest_has_tab(guest) != True:
            self.add_guest_to_tab(guest)
        self.tab[guest] += amount

    def order_drink_on_tab(self, guest, drink):
        self.add_money_to_tab(guest, drink.price)

    def order_food_on_tab(self, guest, food):
        self.add_money_to_tab(guest, food.price)

    def pay_tab(self, guest, room):
        amount = self.tab[guest]
        guest.money -= amount
        self.tab[guest] -= amount
        self.room_take[room] += amount


    def check_room_tab(self, room):
        room_tab = 0
        for key in self.tab:
            if key in room.guests:
                room_tab += self.tab[key] 
        return room_tab
    
    def check_room_take_exists(self, room):
        return self.room_take[room]
    
    def pay_entry_fee(self, guest, room):
        guest.money -= self.entry_fee
        if room in self.room_take.keys():
            self.room_take[room] += self.entry_fee
        else:
            self.room_take[room] = self.entry_fee