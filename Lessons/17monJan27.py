"""
import random
random.seed(random.random())

all_data = []

rows = 5
columns = 10

for _ in range(rows):
	lis2add = []
	for _ in range(columns):
		lis2add += [random.randint(0, 9)]
	all_data.append(lis2add)

for row in range(len(all_data)):
	for column in range(len(all_data[0])):
		print(all_data[row][column], end=" ")
	print("")
"""

strin = input("What would you like to tsify? ")
strin = strin.split(" ")

for i in range(len(strin)):
	strin[i] = strin[i].strip()
res = ""

for word in strin:
	res += f"ts ({word}) "
print(res)