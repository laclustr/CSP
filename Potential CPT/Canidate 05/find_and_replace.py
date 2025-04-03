for _ in range(50):
	print("\n")
input()

print(
"""Welcome to the FFM (Fast File Manager)
Press Return to Start""", end="")
input()

def get_word_start_idxs(txt, key):
	txt = txt.splitlines()
	key_len = len(key)
	idx_list = []

	for line in txt:
		new_idx_line = []
		for char in range(len(line) - key_len + 1):
			if line[char:char + key_len] == key:
				new_idx_line.append(char)
		idx_list.append(new_idx_line)

	return idx_list

def get_occurences(idx_list):
	counter = 0
	if idx_list:
		for line in idx_list:
			for idx in line:
				counter += 1
	return counter

def find_and_replace(file, word, replacement):
	idxs = get_word_start_idxs(file, word)
	file = file.splitlines()
	new_data = []

	for line in range(len(file)):
		line_v = file[line]
		for idx in idxs[line][::-1]:
			line_v = line_v[:idx] + replacement + line_v[idx + len(word):]
		new_data.append(line_v)

	return new_data

sel_file = None

while True:
	try:
		print("\nSelected File:", str(sel_file) if sel_file else "None")
		choice = int(input("""
Enter a Choice:
1. Select a File
2. Count Occurences
3. Find and Replace
4. Print File Contents
5. Exit
"""))
		if choice not in range(1, 6):
			raise ValueError
		match choice:
			case 1:
				user_input = input("Enter a .txt file path: ").strip().replace("\'", "").replace("\"", "")
				try:
					if user_input[len(user_input) - 4:] != ".txt":
						print("File does not end in \".txt\"! Please enter a valid text file path!")
						continue
					with open(user_input, "r") as f:
						sel_file = user_input
				except:
					print("File invalid! Please enter a valid file!")
			case 2:
				if sel_file:
					key = input("Enter a word to count it's occurences: ")
					with open(sel_file, "r") as f:
						print("\n\"" + key + "\" occurs " + str(get_occurences(get_word_start_idxs(f.read(), key))) + " times in the selected file")
				else:
					print("Please select a file first!")
					continue
			case 3:
				if sel_file:
					with open(sel_file, "r") as f:
						txt = f.read()
					word = input("What word would you like to replace: ")
					replacement = input("What would you like to replace the word with: ")
					new_data = find_and_replace(txt, word, replacement)
					with open(sel_file, "w") as f:
						for line in new_data:
							f.write(line)
							if not line is new_data[-1]:
								f.write("\n")
					print(word + " has been replaced with " + replacement)
				else:
					print("Please select a file first!")
					continue
			case 4:
				if sel_file:
					with open(sel_file, "r") as f:
						txt = f.read().splitlines()
						print("\nFile contents of " + str(sel_file) + ":")
						for line in txt:
							print("\t" + line)
				else:
					print("Please select a file first!")
			case 5:
				break
	except ValueError:
		print("\nPlease enter a valid choice!")








