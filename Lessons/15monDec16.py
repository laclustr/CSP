import random
import time
import string
import bisect

start_time = time.time()

def binary_search(lis, key):
	l = 0
	r = len(lis) - 1

	while r >= l:
		mid = (l + r) // 2

		if lis[mid] == key:
			return mid
		elif lis[mid] < key:
			l = mid + 1
		else:
			r = mid - 1

	return -1

nums = []

for i in range(10000):
	nums += [i]

#print(binary_search(nums, 10000))

#Best Case = o(1)
#Worst and Avg. Case log2(n)

random.seed(42)

nums_unsorted = []
for _ in range(10):
	nums_unsorted += [random.randint(0, 100000000000000000000)]
#print(f"Checkpoint: {time.time() - start_time:.4f} seconds")

#3 elementry algorithms;
#selection sort, bubble sort, insertion sort

def swap(li, i, j):
	temp = li[i]
	li[i] = li[j]
	li[j] = temp

def selection_sort(lis):
	for i in range(len(lis)):
		smallest = i
		for j in range(i + 1, len(lis)):
			if lis[j] < lis[smallest]:
				smallest = j

		swap(lis, smallest, i)

#selection_sort(nums_unsorted)
#print(nums_unsorted)

#Efficiency

def counting_sort(arr, exp):
	n = len(arr)
	output = [0] * n
	count = [0] * 10
	for num in arr:
		index = (num // exp) % 10
		count[index] += 1
	for i in range(1, 10):
		count[i] += count[i - 1]
	for i in range(n - 1, -1, -1):
		index = (arr[i] // exp) % 10
		output[count[index] - 1] = arr[i]
		count[index] -= 1
	for i in range(n):
		arr[i] = output[i]

def radix_sort(arr):
	if not arr:
		return arr
	max_num = max(arr)
	exp = 1
	while max_num // exp > 0:
		counting_sort(arr, exp)
		exp *= 10
	return arr

#radix_sort(nums_unsorted)
#print(f"Checkpoint: {time.time() - start_time:.4f} seconds")

def counting_sort_strings(arr, index):
	n = len(arr)
	output = ["" for _ in range(n)]
	count = [0] * 256
	for s in arr:
		char = ord(s[index]) if index < len(s) else 0
		count[char] += 1
	for i in range(1, 256):
		count[i] += count[i - 1]
	for i in range(n - 1, -1, -1):
		char = ord(arr[i][index]) if index < len(arr[i]) else 0
		output[count[char] - 1] = arr[i]
		count[char] -= 1
	for i in range(n):
		arr[i] = output[i]

def radix_sort_strings(arr):
	if not arr:
		return arr
	max_len = max(len(s) for s in arr)
	for i in range(max_len - 1, -1, -1):
		counting_sort_strings(arr, i)
	return arr

def find_string(sorted_list, target):
	index = bisect.bisect_left(sorted_list, target)
	if index < len(sorted_list) and sorted_list[index] == target:
		return index
	return -1

unsorted_strings = []

for _ in range(1000000):
	string = ""
	for i in range(random.randint(5, 20)):
		string += chr(random.randint(97, 122))
	unsorted_strings += [string]

print(f"Checkpoint: {time.time() - start_time:.4f} seconds")

radix_sort_strings(unsorted_strings)
print(f"Checkpoint: {time.time() - start_time:.4f} seconds")

print(find_string(unsorted_strings, input("rand string: ")))









