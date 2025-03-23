import random

random.seed(42)

nums = []

for i in range(10):
	nums.append(random.randint(1, 1000))

def swap(li, i, j):
	temp = li[i]
	li[i] = li[j]
	li[j] = temp

def is_sorted(li):
	for i in range(1, len(li)):
		if li[i] < li[i - 1]:
			return False

	return True

def selection_sort(li):
	for i in range(len(li)):
		smallest = i

		for j in range(i + 1, len(li)):
			if li[j] < li[smallest]:
				smallest = j
		swap(li, i, smallest)

def bubble_sort(li):
	for _ in range(len(li)):
		for i in range(len(li) - 1):
			if li[i] > li[i + 1]:
				swap(li, i, i + 1)

def bubble_sort_re1(li):
	for _ in range(len(li) - 1):
		for i in range(len(li) - 1):
			if li[i] > li[i + 1]:
				swap(li, i, i + 1)

def bubble_sort_re2(li):
	for j in range(len(li)):
		for i in range(len(li) - 1 - j):
			if li[i] > li[i + 1]:
				swap(li, i, i + 1)

def bubble_sort_re3(li):
	for j in range(len(li)):
		has_swapped = False
		for i in range(len(li) - 1 - j):
			if li[i] > li[i + 1]:
				swap(li, i, i + 1)
				has_swapped = True
		if not has_swapped:
			return

# Insertion Sort

def insertion_sort(li):
	for i in range(1, len(li)):
		j = i

		while j > 0 and li[j] < li[j - 1]:
			swap(li, j, j - 1)
			j -= 1

print(nums)
insertion_sort(nums)
print(nums)













