import os

userName = input("Name: ")
while not userName.isalpha():
	os.system('clear')
	userName = input("Name: ")
if userName == "Shutdown":
	os.system('sudo shutdown -h now')

userAge = input("Age: ")
while not userAge.isdigit():
	os.system('clear')
	userAge = input("Age: ")

print("Hello, " + userName)

if int(userAge) < 13:
	print('You must be over 13 to use this app')
else:
	print('Welcome to Skibidi Studios!')	