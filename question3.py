class Band:

	def __init__(self, genre="rock", name='Unknown'):
		self.genre = genre
		self.name = name

class RollingStones(Band):
	def __init__(self, genre="rock"):
		Band.__init__(self, genre,name="Rolling Stones")
		self.genre = genre
	def __str__(self):
		return self.name
class RedHotChiliPeppers(Band):
	def __init__(self, genre="rock"):
		Band.__init__(self, genre, name="Red Hot Chili Peppers")
		self.genre = genre
	def __str__(self):
		return self.name

roll = RollingStones()
rchp = RedHotChiliPeppers("funk")
print(roll, roll.genre)
print(rchp, rchp.genre)