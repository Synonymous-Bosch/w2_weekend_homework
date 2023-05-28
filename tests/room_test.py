import unittest
from classes.room import *
from classes.guest import *
from classes.song import *
from classes.bar import *
from classes.drink import *
from classes.food import *

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.guest1 = Guest("Mario Mario", 45.20, "That's Amore")
        self.guest2 = Guest("Luigi Mario", 20.00, "Shaddap Your Face")
        self.guest3 = Guest("Toad", 4.20, "Mushroom Men")
        self.song1 = Song("That's Amore", "Dean Martin")
        self.song2 = Song("Shaddap Your Face", "Joe Dolce")
        self.song3 = Song("Mushroom Men", "Les Claypool")
        songs = [self.song1]
        guests = [self.guest1]
        drinks = []
        foods = []
        self.bar = Bar(drinks, foods)
        self.room1 = Room(1, 6, guests, songs)
        self.room2 = Room(2, 1, guests, songs)
 

    def test_room_has_number(self):
        self.assertEqual(1, self.room1.number)

    def test_room_has_guests(self):
        self.assertEqual(self.guest1, self.room1.guests[0])

    def test_room_has_songs(self):
        self.assertEqual(self.song1, self.room1.songs[0])

    def test_check_in(self):
        self.room1.check_in(self.guest2)
        self.assertEqual(self.room1.guests[1], self.guest2)

    def test_check_out(self):
        self.room1.check_out(self.guest1)
        self.assertEqual(0, len(self.room1.guests))

    def test_add_song_to_room(self):
        self.room1.add_song_to_room(self.song2)
        self.assertEqual(self.song2, self.room1.songs[1])

    def test_check_room_capacity(self):
        self.room1.check_room_capacity()
        self.assertEqual(6, self.room1.capacity)

    def test_check_in_room_at_capacity(self):
        result = self.room2.check_in(self.guest2)
        self.assertEqual("Sorry. Room's at capacity", result)
        self.assertEqual(1, len(self.room2.guests))



    def test_guest_can_not_afford_entry_fee(self):
        result = self.room1.guest_can_afford_entry_fee(self.guest3)
        self.assertEqual(False, result)

    def test_guest_can_afford_entry_fee(self):
        result = self.room1.guest_can_afford_entry_fee(self.guest1)
        self.assertEqual(True, result)

    def test_check_in_guest_can_not_afford(self):
        result = self.room1.check_in(self.guest3)
        self.assertEqual("Get out of here, deadbeat", result)
        self.assertEqual(1, len(self.room2.guests))

    def test_favourite_song_on_playlist(self):
        result = self.room1.favourite_song_on_playlist()
        self.assertEqual('Mario Mario shouts "Wahoo!"', result)




