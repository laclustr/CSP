import random

class Dice:
	def __init__(self, sides=6):
		self.sides = ["L", "R", ""]

	def roll(self):
		return random.randint(1, self.sides)

	def __str__(self):
		return f"A {self.sides} sided dice."

lis = [1,2,3]
print(lis[-1])