import random

#MC Problem
def experiment():
	def_parts = 0

	for i in range(10):
		if random.random() < 0.1:
			def_parts += 1

	return def_parts >= 3

def probability():
	successes = 0
	simulations = 1000000

	for i in range(simulations):
		if experiment():
			successes += 1

	return successes / simulations

print(probability())