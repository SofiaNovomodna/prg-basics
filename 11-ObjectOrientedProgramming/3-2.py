class Song:
   def __init__(self, Performer, Title, Album, Year):
      self.Performer = Performer
      self.Title = Title
      self.Album = Album
      self.Year = Year

   def __str__(self):
        return f"Performer: {self.Performer:<20}\nTitle: {self.Title:<30}\nAlbum: {self.Album:<30}\nYear: {self.Year}"

# Creating instances of the Song class (not Car class)
song1 = Song("Ed Sheeran", "Hearts Don't Break Around Here", 'Divide', 2017)
song2 = Song("Queen", "Bohemian Rhapsody", 'A Night at the Opera', 1975)

# Print the objects (songs)
print(song1)
print()
print(song2)