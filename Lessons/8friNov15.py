def rem_aeiou_rev(string):
	res = ""
	i = len(string) - 1
	while i >= 0:
		if not (string[i] == "a" or
				string[i] == "o" or
				string[i] == "u" or
				string[i] == "e" or
				string[i] == "i"):
			res = res + string[i]

		i -= 1

	return res