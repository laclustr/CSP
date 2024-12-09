nums = [2, 3, 1, 4, 6, 10, 12]
students = ["hehe", "bdf", "brad"]

def average(nums):
	nsum = 0
	for i in nums:
		nsum += i
	return nsum / len(nums)

##############################

def total_sum(nums):
	nsum = 0
	for i in nums:
		nsum += i
	return nsum

##############################

def longthank(name, k):
	return len(name) > k

def count_name(names, k):
	counter = 0

	for i in names:
		if longthank(i, k):
			counter += 1

	return counter

###############################

students[0] = "grant"
print(students)

"""
Will not work:

strin = "grant"
strin[0] = "r"

Strings aren't mutable, arrays are.
"""

print(id(students))


