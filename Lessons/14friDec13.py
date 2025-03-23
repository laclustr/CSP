data = open("data.txt", "r").read()
string_lines = data.splitlines()

left_nums = []
right_nums = []

for line in string_lines:
	line_list = line.split()
	left_nums.append(int(line_list[0]))
	right_nums.append(int(line_list[1]))

left_nums.sort()
right_nums.sort()

total = 0
for i in range(len(left_nums)):
	total += abs(left_nums[i] - right_nums[i])

print(total)
