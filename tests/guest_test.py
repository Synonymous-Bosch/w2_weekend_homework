import unittest
from classes.guest import *
from classes.song import *

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest1 = Guest("Mario Mario", 45.20, "That's Amore")
        self.song1 = Song("That's Amore", "Dean Martin")
        songs = [self.song1]
        guests = [self.guest1]
        self.room1 = Room(1, 6, guests, songs)
        cheese = 10

    def test_guest_has_name(self):
        self.assertEqual("Mario Mario", self.guest1.name)

    def test_guest_has_money(self):
        self.assertEqual(45.20, self.guest1.money)

    def test_guest_has_favourite_song(self):
        self.assertEqual("That's Amore", self.guest1.favourite_song)


