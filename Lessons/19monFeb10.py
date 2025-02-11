player_dict = {
	"name": "Kanye West",
	"job": "rapper",
	"age": 47
	}

class Player:
	def __init__(self, name, job, age):
		self.name = name
		self.job = job
		self.age = age
player_class = Player("Kanye West", "Rapper", 47)

print(player_dict[name])
print(player_class.name)
		