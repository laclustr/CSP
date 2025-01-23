def ends_with(tlist, substring):
	resultList = []

	for i in tlist:
		diff = len(i) - len(substring)

		if i[diff:len(i)] == substring:
			resultList.append(i)

	return resultList

def index_of(string, substring):
	for i in range(len(string) - len(substring) + 1):
		if string[i:(i + len(substring))] == substring:
			return i

	return -1

def contains(list1, substring):
	resultList = []

	for i in list1:
		if index_of(i, substring) >= 0:
			resultList.append(i)

	return resultList

print(contains(["hello.txt", "welcome.pdf", "wsg.py", "fein.txt"], "e"))

