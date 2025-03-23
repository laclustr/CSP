"""
	dictonaries are lowk trash, js use classes instead
	for dics, functions were unique to their respective dictionaries
	Classes fix this
"""
dic_songv = {"artist": "Kanye", "title": "Runaway", "length": 600}

class CollabSong:
	def __init__(self, artists, titles, length):
		self.artists = artists
		self.titles = titles
		self.length = length

	def __iter__(self):
		return iter(vars(self).values())

class Song:
	def __init__(self, artist, title, length):
		self.artist = artist
		self.title = title
		self.length = length

	def __iter__(self):
		return iter(vars(self).values())

	def __add__(self, other):
		return CollabSong((self.artist, other.artist), (self.title, other.title), self.length + other.length)

kanyesong = Song("Kanye", "Runaway", 600)
jayzsong = Song("jayz", "Otis", 200)

print(list(kanyesong))
print(list(kanyesong + jayzsong))






