with open("20Feb_babynames.txt", "r") as f:
	babynames = f.read().split()

print(babynames[0])

"""
#Overwrites/creates a file
with open("output.txt", "w") as f:
	newtxt = ""
	for name in babynames:
		newtxt += name + "\n"
	f.write(newtxt)

#Appends to a file
with open("output.txt", "a") as f:
	f.write("Kanye")
"""
