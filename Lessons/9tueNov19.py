import random

def longestWord(string):
	curr = ""
	longest = ""

	for letter in string:
		if letter != " ":
			curr += letter
		else:
			if len(curr) > len(longest):
				longest = curr
			curr = ""

	if len(curr) > len(longest):
		longest = curr

	return longest

def longestWord2(string):
	longest = ""

	i = 0
	for j in range(len(string)):
		if string[j] == " ":
			new_word = string[i:j]

			if len(new_word) > len(longest):
				longest = new_word

			i = j + 1

	new_word = string[i:len(string)]
	if len(new_word) > len(longest):
		longest = new_word

	return longest

def experiment(n_sixes):
	n_rolls = n_sixes * 6
	counter = 0

	for i in range(n_rolls):
		if random.randint(1, 6) == 6:
			if counter == n_sixes:
				return True
			counter += 1

	return False
def get_prob(i, trials):
	successes = 0
	for t in range(trials):
		if experiment(i):
			successes += 1

n_trials = 10000000000
for i in range(1, 4):
	print(str(i) + " sixes in " + str(i * 6) + " rolls: " + str(get_prob(i, n_trials)))