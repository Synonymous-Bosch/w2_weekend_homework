import unittest
from classes.song import *

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song1 = Song("That's Amore", "Dean Martin")

    def test_song_has_title(self):
        self.assertEqual("That's Amore", self.song1.title)

    def test_song_has_artist(self):
        self.assertEqual("Dean Martin", self.song1.artist)