userName = input("Name: ")
while not userName.isalpha():
	userName = input("Name: ")
print("Hello, " + userName)