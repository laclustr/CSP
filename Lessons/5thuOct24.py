def calc(x, y, z):
	if x == "1":
		return y + z
	elif x == "2":
		return y - z
	elif x == "3":
		return y / z
	elif x == "4":
		return y * z
	else:
		return "Please enter a valid operator!"

calcMode = input("Pick a number with it's corresponding operator:\n Add) 1\n Sub) 2\n Div) 3\n Mul) 4\n")
num1 = int(input("\nFirst number: "))
num2 = int(input("Second number: "))

answer = calc(calcMode, num1, num2)
if answer != "Please enter a valid operator!":
	print("\nYour answer is: " + str(answer))
else:
	print("\n" + answer)