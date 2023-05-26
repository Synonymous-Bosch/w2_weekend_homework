class Room:
    def __init__(self, number, capacity, guests, songs):
        self.number = number
        self.capacity = capacity
        self.guests = guests
        self.songs = songs
        self.entry_fee = 5.00

    def check_in(self, guest):
        if self.check_room_capacity() > len(self.guests) and self.guest_can_afford_entry_fee(guest) == True:
            self.guests.append(guest)
        elif self.check_room_capacity() > len(self.guests):
            return "Get out of here, deadbeat"
        else:
            return "Sorry. Room's at capacity"

    def check_out(self, guest):
        self.guests.remove(guest)

    def add_song_to_room(self, song):
        self.songs.append(song)

    def check_room_capacity(self):
        return self.capacity
    
    def pay_entry_fee(self, guest):
        guest.money -= self.entry_fee

    def guest_can_afford_entry_fee(self, guest):
        if guest.money >= self.entry_fee:
            return True
        else:
            return False
        
    def favourite_song_on_playlist(self):
        for guest in self.guests:
            for song in self.songs:
                if guest.favourite_song == song.title:
                    return f'{guest.name} shouts "Wahoo!"'