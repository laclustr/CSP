class Food:
	def __init__(self, name):
		self.name = name
		self.amount = 1

try:
	lis = []
	while True:
		food = input().strip().upper()
		if not lis:
			lis += [Food(name = food)]
		else:
			for i in range(len(lis)):
				if lis[i].name == food:
					lis[i].amount += 1
					break
			else:
				lis += [Food(name = food)]
except EOFError:
	pass

for i in lis:
	print(f"{i.amount} {i.name}") 