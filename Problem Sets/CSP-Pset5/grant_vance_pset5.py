import random

class Cookie:
	def __init__(self, cookie_type, price):
		self.cookie_type = cookie_type
		self.price = price
		self.bites_left = 3

	def bite(self):
		if self.bites_left > 0:
			self.bites_left -= 1
			print("chomp")

	def is_eaten(self):
		if self.bites_left > 0:
			return False
		else:
			return True

	def __repr__(self):
		return f"Cookie({self.cookie_type}, {self.price})"

class Jar:
	def __init__(self, capacity):
		self.capacity = capacity
		self.cookies = []

	def deposit(self, other):
		if len(self.cookies) >= self.capacity:
			raise ValueError
		if other.bites_left == 0:
			raise ValueError
		self.cookies.append(other)

	def withdraw(self, n_or_type):
		if isinstance(n_or_type, int):
			if n_or_type > len(self.cookies):
				raise ValueError
			rem_cookie_list = []
			for i in range(n_or_type):
				rem_cookie_list.append(self.cookies.pop(random.randint(0, len(self.cookies) - 1)))

			return rem_cookie_list
		else:
			for cookie_idx in range(len(self.cookies)):
				if self.cookies[cookie_idx].cookie_type == n_or_type:
					return self.cookies.pop(cookie_idx)
			raise ValueError

	def size(self):
		return len(self.cookies)

	def cookie_counter(self):
		dic = {}
		for cookie_idx in range(len(self.cookies)):
			if self.cookies[cookie_idx].cookie_type in dic.keys():
				dic[self.cookies[cookie_idx].cookie_type] += 1
			else:
				dic[self.cookies[cookie_idx].cookie_type] = 1
		return dic

	def value(self):
		total = 0
		for cookie in self.cookies:
			total += cookie.price

		return total

	def bites_left(self):
		total = 0
		for cookie in self.cookies:
			total += cookie.bites_left

		return total

	def __str__(self):
		return f"{len(self.cookies)}"