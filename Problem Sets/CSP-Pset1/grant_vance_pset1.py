#Problem 1
def count_e(string):
	ecount = 0

	for i in string:
		if i == "e" or i == "E":
			ecount += 1
	return ecount

#Problem 2
def ends_with(string, substring):
	diff = len(string) - len(substring)

	if string[diff:len(string)] == substring:
		return True
	return False

#Problem 3
def reverse_string(string):
	rev_string = ""

	for i in string:
		rev_string = i + rev_string

	return rev_string

#Problem 4
def sum_between(a, b):
	total = 0

	for i in range(a, b + 1):
		total += i

	return total

#Problem 5
def index_of(string, substring):
	for i in range(len(string) - len(substring) + 1):
		if string[i:(i + len(substring))] == substring:
			return i

	return -1

#Problem 6
def count_long_char(string):
	max_len = 1
	curr_len = 1

	for i in range(1, len(string)):
		if string[i] == string[i - 1]:
			curr_len += 1
			if curr_len > max_len:
				max_len = curr_len
		else:
			curr_len = 1

	return max_len

#Problem 7
def is_good_password(password):
	if len(password) < 10:
		return False

	caps = False
	lower = False
	special = False

	for i in password:
		if ord(i) >= 65 and ord(i) <= 90:
			caps = True
		elif ord(i) >= 97 and ord(i) <= 122:
			lower = True
		elif ((ord(i) >= 33 and ord(i) <= 47)
			or (ord(i) >= 58 and ord(i) <= 64)
			or (ord(i) >= 91 and ord(i) <= 96)
			or (ord(i) >= 123 and ord(i) <= 126)):
			special = True

	if caps and lower and special:
		return True
	return False

#Problem 8
def harshad_numbers(n):
	count = 0

	for i in range(1, n + 1):
		lnum = 0
		tnum = i

		while tnum > 0:
			lnum += tnum % 10
			tnum //= 10

		if i % lnum == 0:
			count += 1
	return count

#Problem 9
def count_digits(n):
	if n < 0:
		n = n * -1

	if n < 10:
		return 1

	count = 0

	while n > 0:
		n = n // 10
		count += 1

	return count

#Problem 10
def upper_string(string):
	result = ""
	for i in string:
		asc = ord(i)
		if not (asc >= 97 and asc <= 122):
			result += i
		else:
			result += chr(asc - 32)

	return result

#Problem 11
def caesar_encrypt(string, n):
	string = upper_string(string)

	result = ""

	for i in string:
		asc = ord(i)
		if not (asc >= 65 and asc <= 90):
			result += i
		else:
			shift = asc + n
			if shift > 90:
				shift = (shift - 91) + 65
			result += chr(shift)

	return result

#Problem 12
def caesar_decrypt(string, n):
	string = upper_string(string)
	result = ""

	for i in string:
		asc = ord(i)
		if not (asc >= 65 and asc <= 90):
			result += i
		else:
			shift = asc - n

			if shift < 65:
				shift = (shift + 26)

			result += chr(shift)

	return result

#Problem 13
def my_pow(x, a):
	result = 1

	while a > 0:
		result *= x
		a -= 1

	return result

#Problem 14
def my_factorial(n):
	result = 1

	if n == 0:
		return result

	for i in range(1, n + 1):
		result *= i

	return result

#Problem 15
def double_factorial(n):
	result = 1

	if n == 0 or n == 1:
		return result

	for i in range(n, 0, -2):
		result *= i

	return result

#Problem 16
def is_palindrome(string):
	result = ""

	for i in string:
		result = i + result
	if string == result:
		return True

	return False

#Problem 17
def my_sqrt(x):
	t = x

	while abs(t ** 2 - x) > 10 ** -15:
		t = (t + x / t) / 2

	return t

#Problem 18
def find_and_replace(string, target, replacement):
	if index_of(string, target) == -1:
		return False

	result = ""

	i = 0
	while i < len(string):
		if string[i:i + len(target)] == target:
			result += replacement
			i += len(target)
		else:
			result += string[i]
			i += 1

	return result

#Problem 19
def fib(n):
	if n == 1:
		return 1

	num1 = 0
	num2 = 1

	i = 2

	while i <= n:
		temp = num2
		num2 += num1
		num1 = temp

		i += 1

	return num2

#Problem 20
def run_length_encode(string):
	result = ""
	count = 1

	for i in range(1, len(string)):
		if string[i] == string[i - 1]:
			count += 1
		else:
			result += string[i - 1] + str(count)
			count = 1

	result += string[len(string) - 1] + str(count)

	return result

#Problem 21
def run_length_decode(string):
	result = ""

	for i in range(0, len(string), 2):
		result += string[i] * int(string[i + 1])

	return result

#Problem 22
def are_anagrams(string1, string2):
	if len(string1) != len(string2):
		return False

	pstring1 = string1
	pstring2 = string2

	for i in string1:

		if index_of(pstring1, i) >= 0:
			pstring1 = find_and_replace(pstring1, i, "")
			if index_of(pstring2, i) >= 0:
				pstring2 = find_and_replace(pstring2, i, "")
			else:
				return False
		else:
			return False

	return True

#Problem 23
def remove_duplicates(string):
	seen = ""
	result = ""

	for i in string:
		if i not in seen:
			seen += i
			result += i

	return result

#Problem 24
def my_exp(x):
	result = 1
	term = 1
	iterations = 1

	while abs(term) >= (10**-15):
		powxk = 1
		factk = 1

		for j in range(1, iterations + 1):
			powxk *= x
			factk *= j

		term = powxk / factk
		result += term
		iterations += 1

	return result

#Problem 25
def make_squares(n):
	firstOrlast = True
	iterations = n
	result = ""

	while iterations > 1:
		if firstOrlast:
			result += "*" * n + " " + "*" * n + "\n"
			firstOrlast = False
		else:
			result += "*" * n + " " + "*" + " " * (n - 2) + "*" + "\n"
		iterations -= 1

	result += "*" * n + " " + "*" * n
	return result

#Problem 26
def make_hollow_diamond(n):
	result = ""
	iterations = n

	for i in range(iterations):
		row = " " * (iterations - i - 1)

		if i == 0:
			row += "*"
		else:
			row += "*" + " " * (2 * i - 1) + "*"

		result += row + "\n"

	for i in range(iterations - 2, -1, -1):
		row = " " * (iterations - i - 1)

		if i == 0:
			row += "*"
		else:
			row += "*" + " " * (2 * i - 1) + "*"

		result += row + "\n"

	return result

#Problem 27
def make_diamond(n):
	result = ""
	iterations = n

	for i in range(iterations):
		row = " " * (iterations - i - 1)

		row += "*" * (2 * i + 1)

		result += row + "\n"

	for i in range(iterations - 2, -1, -1):
		row = " " * (iterations - i - 1)

		row += "*" * (2 * i + 1)

		result += row + "\n"

	return result

import random

#Problem MC1
def k_consecutive(p, n, k):
	simulations = 10000000
	successes = 0

	for i in range(simulations):
		heads = 0
		enoughHeads = False

		for j in range(n):
			if random.random() < p:
				heads += 1

				if heads >= k:
					enoughHeads = True
			else:
				heads = 0

		if enoughHeads:
			successes += 1

	return successes / simulations

#Problem MC2
def p_unfair_coin(n, g, p, n_heads, n_flips):
	simulations = 1000
	biCoins = n - g

	biCounter = 0
	tCounter = 0

	for i in range(simulations):
		biased = random.random() < (biCoins / n)

		if biased:
			probHead = p
		else:
			probHead = 0.5

		headCount = 0
		for i in range(n_flips):
			if random.random() < probHead:
				headCount += 1

		if headCount == n_heads:
			tCounter += 1

			if biased:
				biCounter += 1

	if tCounter == 0:
		return 0

	return biCounter / tCounter

#Problem MC3
def draw_all_good_cards(n, g, turn):
	simulations = 1000000
	successes = 0

	for i in range(simulations):
		bCards = n - g
		gCards = g

		gCardDraws = 0

		for j in range(turn):
			if random.random() < gCards / (gCards + bCards):
				gCardDraws += 1
				gCards -= 1
			else:
				bCards -= 1

		if gCardDraws == g:
			successes += 1

	return successes / simulations